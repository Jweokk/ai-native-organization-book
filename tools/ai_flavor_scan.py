#!/usr/bin/env python3
"""AI 味检测扫描（detect_only，基于 dai/Say-It-Human 的 24 维图谱）。

用法：
    python3 tools/ai_flavor_scan.py            # 默认：第10章10节 + 第2章 + 第7章
    python3 tools/ai_flavor_scan.py --ch 02    # 只扫指定章节（如 02）

说明：
- 只检测不改写（dai 的 detect_only 模式）
- 检测结果仅供参考：书/综述体裁存在合理误报（结构对称、术语密度等），
  改造决策以人工判断为准，不自动采纳任何改写建议
"""
import json, os, re, subprocess, sys, time
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PROMPT_FILE = Path("/home/ubuntu/workspace/say-it-human-web/app/prompt.py")

def load_prompt():
    src = PROMPT_FILE.read_text(encoding="utf-8")
    sp = re.search(r'SYSTEM_PROMPT = """(.*?)"""', src, re.S).group(1)
    ds = re.search(r'DETECT_ONLY_SUFFIX = """(.*?)"""', src, re.S).group(1)
    return sp + "\n" + ds

def read_key():
    # 用绝对路径（HOME 环境变量在不同 profile 下有坑）；跳过空值（tokens.env 有重复空行）
    env = Path("/home/ubuntu/.hermes/tokens.env")
    for line in env.read_text().splitlines():
        if line.startswith("DEEPSEEK_API_KEY="):
            v = line.split("=", 1)[1].strip()
            if v:
                return v
    return None

def call_deepseek(system, user, model="deepseek-v4-flash", key=None):
    # deepseek-v4-flash 是推理模型：max_tokens 必须够大（推理+输出共享预算），
    # 否则 content 为空（全部被推理吃掉）。4000+ 才保证 JSON 输出完整。
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "temperature": 0.3,
        "max_tokens": 6000,
    }
    r = subprocess.run(
        ["curl", "-s", "--max-time", "180", "-X", "POST",
         "https://api.deepseek.com/v1/chat/completions",
         "-H", f"Authorization: Bearer {key}",
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload, ensure_ascii=False)],
        capture_output=True, text=True, timeout=200)
    try:
        d = json.loads(r.stdout)
        return d["choices"][0]["message"]["content"]
    except Exception:
        return f"ERROR: {r.stdout[:300]}"

def extract_json(text):
    m = re.search(r'\{.*\}', text, re.S)
    if not m:
        return {"parse_error": text[:200]}
    try:
        return json.loads(m.group(0))
    except Exception:
        return {"parse_error": text[:200]}

def split_ch10(text):
    """按 ## 10.x 切分第 10 章"""
    parts = re.split(r'\n(?=## 10\.)', text)
    out = []
    for p in parts:
        m = re.match(r'## 10\.(\d+) (.+)', p)
        if m:
            out.append((f"10.{m.group(1)} {m.group(2)}", p))
    return out

def main():
    targets = []
    ch_filter = None
    model = "deepseek-v4-flash"  # 默认当前配置模型
    if "--ch" in sys.argv:
        ch_filter = sys.argv[sys.argv.index("--ch") + 1]
    if "--model" in sys.argv:
        model = sys.argv[sys.argv.index("--model") + 1]

    book = BASE / "book"
    # 第 10 章按节
    if not ch_filter or ch_filter == "10":
        ch10 = (book / "10-第10章-行业篇.md").read_text(encoding="utf-8")
        targets += split_ch10(ch10)
    # 第 2 章、第 7 章整章
    for fname, label in [("02-第2章-什么是AI原生组织.md", "第2章 什么是AI原生组织"),
                         ("07-第7章-案例集.md", "第7章 案例集")]:
        if not ch_filter or ch_filter in fname:
            targets.append((label, (book / fname).read_text(encoding="utf-8")))

    system = load_prompt()
    key = read_key()
    if not key:
        print("DEEPSEEK_API_KEY 未找到")
        sys.exit(1)

    print(f"扫描目标：{len(targets)} 节\n")
    report = []
    totals = {"score": [], "issues": {}}
    for i, (label, text) in enumerate(targets, 1):
        # 检测文本截断保护
        user = text[:14000] if len(text) > 14000 else text
        print(f"[{i}/{len(targets)}] 检测中：{label}（{len(user)} 字）...")
        raw = call_deepseek(system, user, model=model, key=key)
        result = extract_json(raw)
        oa = result.get("original_analysis", {}) if isinstance(result, dict) else {}
        score = oa.get("ai_concentration_score")
        if score is not None:
            totals["score"].append(score)
            for iss in oa.get("issues", []):
                cat = iss.get("category", "?")
                totals["issues"][cat] = totals["issues"].get(cat, 0) + 1
        report.append((label, result, oa))
        time.sleep(1)

    # 汇总输出
    lines = ["# 本书 AI 味检测报告（detect_only，仅供参考）", ""]
    lines.append(f"扫描日期：{time.strftime('%Y-%m-%d')}")
    lines.append(f"检测范围：{len(targets)} 节")
    if totals["score"]:
        avg = sum(totals["score"]) / len(totals["score"])
        lines.append(f"平均 AI 味浓度：{avg:.0f}/100（{max(totals['score'])} 最高 / {min(totals['score'])} 最低）")
        lines.append("")
        lines.append("## 问题维度分布（出现次数 top）")
        for cat, cnt in sorted(totals["issues"].items(), key=lambda x: -x[1])[:15]:
            lines.append(f"- {cat}: {cnt}")
    lines.append("")
    lines.append("## 分节结果")
    for label, result, oa in report:
        lines.append(f"\n### {label}")
        lines.append(f"浓度: {oa.get('ai_concentration_score')}/100 [{oa.get('ai_concentration_label')}]")
        lines.append(f"总评: {oa.get('summary', '')}")
        for iss in oa.get("issues", [])[:4]:
            ex = (iss.get("examples") or ["-"])[0][:80]
            lines.append(f"- [{iss.get('severity')}/10 ×{iss.get('count')}] {iss.get('category')}: {ex}")
        ra = result.get("rewritten_analysis", {}) if isinstance(result, dict) else {}
        imps = ra.get("improvements", [])
        if imps:
            lines.append(f"  → 建议: {'；'.join(imps[:3])}")
    out = BASE / "tools" / "ai-flavor-report.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n报告已保存：{out}")

if __name__ == "__main__":
    main()
