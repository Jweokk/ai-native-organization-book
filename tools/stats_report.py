#!/usr/bin/env python3
"""《AI 原生组织》项目统计报告（供每周日 cron 调用）。

收集：
1. GitHub 仓库：stars / forks / watchers / 14天 clones / 14天 views（gh api）
2. Cloudflare 域名：HTTP 请求数与唯一访客（GraphQL analytics，需 Zone Analytics 读权限；
   无权限时在报告中提示如何开通）
3. 历史快照：tools/stats_history.json 每周追加，报告给出"本周 vs 上周"对比与累计

用法：python3 tools/stats_report.py
输出：markdown 文本（可直接放进 cron 报告）
"""
import json, os, subprocess, sys
from datetime import datetime, timedelta

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY = os.path.join(BASE, "tools", "stats_history.json")
REPO = "Jweokk/ai-native-organization-book"
ZONE = "a79e9241a26834e33effd858a68ee828"  # fly2ai.top

def gh_json(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None

def cf_analytics():
    """CF GraphQL zone analytics（fly2ai.top 全站总量）。
    注：httpRequests1dGroups 的 filter 不支持按 host/路径过滤，
    单站点精确统计需 CF Web Analytics（Dashboard 创建并查看）。
    """
    import os as _os
    token = None
    env_path = os.path.expanduser("~/.hermes/tokens.env")
    if os.path.exists(env_path):
        for line in open(env_path):
            line = line.strip()
            if line.startswith("CF_ZONE_TOKEN="):
                token = line.split("=", 1)[1].strip().strip('"').strip("'")
                break
    if not token:
        return None, "CF token 未找到"
    today = datetime.now().strftime("%Y-%m-%d")
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    query = (
        '{ viewer { zones(filter: {zoneTag: "%s"}) { '
        "httpRequests1dGroups(limit: 8, filter: {date_geq: \"%s\"}) { "
        "dimensions { date } sum { requests } uniq { uniques } } } } }"
    ) % (ZONE, week_ago)
    r = subprocess.run(
        ["curl", "-s", "--max-time", "20", "-X", "POST",
         "https://api.cloudflare.com/client/v4/graphql",
         "-H", "Authorization: Bearer " + token,
         "-H", "Content-Type: application/json",
         "--data", json.dumps({"query": query})],
        capture_output=True, text=True, timeout=40)
    try:
        d = json.loads(r.stdout)
    except Exception:
        return None, "CF API 响应解析失败"
    if not d.get("data"):
        err = d.get("errors", [{}])[0].get("message", "未知错误")
        return None, err
    groups = d["data"]["viewer"]["zones"][0]["httpRequests1dGroups"]
    return groups, None


def load_history():
    if os.path.exists(HISTORY):
        try:
            return json.load(open(HISTORY))
        except Exception:
            return []
    return []

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    lines = []
    lines.append(f"### 📊 《AI 原生组织》项目统计（{today}）")
    lines.append("")

    # ── GitHub ──
    repo = gh_json(f"repos/{REPO}")
    if repo:
        lines.append(f"**GitHub 仓库** [github.com/Jweokk/ai-native-organization-book](https://github.com/Jweokk/ai-native-organization-book)")
        lines.append(f"- ⭐ Stars: {repo.get('stargazers_count', 0)} ｜ 🍴 Forks: {repo.get('forks_count', 0)} ｜ 👀 Watchers: {repo.get('subscribers_count', 0)}")
        lines.append(f"- 📅 最近推送: {repo.get('pushed_at', '')[:10]}")
    else:
        lines.append("**GitHub 仓库**：API 获取失败")
    clones = gh_json(f"repos/{REPO}/traffic/clones")
    views = gh_json(f"repos/{REPO}/traffic/views")
    if clones:
        lines.append(f"- 📥 克隆（近14天）: {clones.get('count', 0)} 次 / {clones.get('uniques', 0)} 人")
    if views:
        lines.append(f"- 👁 浏览（近14天）: {views.get('count', 0)} 次 / {views.get('uniques', 0)} 人")
    lines.append("")

    # ── CF 域名 ──
    groups, err = cf_analytics()
    if groups:
        total = sum(g["sum"]["requests"] for g in groups)
        uniq = sum(g["uniq"]["uniques"] for g in groups)
        lines.append(f"**域名站点（fly2ai.top 全站，含全部子项目）** [aiorg.fly2ai.top](https://aiorg.fly2ai.top)")
        lines.append(f"- 🌐 近7天 HTTP 请求: {total:,} 次 / 唯一访客: {uniq:,}")
        # 按天明细
        daily = ", ".join(f"{g['dimensions']['date'][5:]}:{g['sum']['requests']}" for g in groups[-7:])
        lines.append(f"- 📈 按天: {daily}")
        lines.append("- 📄 注：单站点/PDF 精确统计需 CF Web Analytics（Dashboard 查看）")
    else:
        reason = err or "未知"
        lines.append(f"**域名站点**：⚠️ CF 统计未启用（{reason[:80]}）")
        lines.append("- 开通方法：Cloudflare Dashboard → My Profile → API Tokens → 编辑该 token → 添加权限 **Zone Analytics → Read**（zone: fly2ai.top），保存后下期自动生效")
    lines.append("")

    # ── 历史快照 ──
    history = load_history()
    snap = {"date": today}
    if repo:
        snap["stars"] = repo.get("stargazers_count", 0)
    if clones:
        snap["clones_14d"] = clones.get("count", 0)
        snap["clones_uniq_14d"] = clones.get("uniques", 0)
    if views:
        snap["views_14d"] = views.get("count", 0)
        snap["views_uniq_14d"] = views.get("uniques", 0)
    if groups:
        snap["cf_req_7d"] = sum(g["sum"]["requests"] for g in groups)
        snap["cf_uniq_7d"] = sum(g["uniq"]["uniques"] for g in groups)
    history.append(snap)
    if len(history) > 16:
        history = history[-16:]
    with open(HISTORY, "w") as f:
        json.dump(history, f, ensure_ascii=False, indent=1)

    if len(history) >= 2:
        prev = history[-2]
        diffs = []
        for k, label in [("stars", "Stars"), ("views_14d", "浏览(14d)"), ("clones_14d", "克隆(14d)")]:
            if k in prev and k in snap:
                d = snap[k] - prev[k]
                sign = "+" if d > 0 else ""
                diffs.append(f"{label} {sign}{d}")
        if diffs:
            lines.append(f"**较上周**: {' ｜ '.join(diffs)}")
        lines.append(f"**累计快照**: 已记录 {len(history)} 周")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    print(main())
