#!/usr/bin/env python3
"""每周更新发布流水线（供 cron LLM agent 调用，或手动执行）。

用法：
    .venv/bin/python tools/update_book.py --title "v1.0.1 更新标题" --notes "更新说明（可多行，每行一个要点）"

流程：
    1. VERSION patch+1（或 --version 指定完整版本号）
    2. CHANGELOG.md 头部插入新版本条目
    3. book/13-附录C-版本历史与更新说明.md 追加条目
    4. 重新生成整本 PDF（tools/build_pdf.py）
    5. mkdocs build（站点静态文件）
    6. git commit + push main（GitHub Actions 会自动部署 Pages）
    7. 写完成标记 .last-update.json（防止 cron 重复执行/超时重跑）

注意：
    - 慢任务内部 timeout：本脚本单次执行控制在 5 分钟内，超时由 cron 层兜底
    - 幂等：执行前检查 .last-update.json 的时间戳，同一天重复调用直接退出
"""
import argparse, json, os, re, subprocess, sys
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION_FILE = os.path.join(BASE, "VERSION")
CHANGELOG = os.path.join(BASE, "CHANGELOG.md")
APPENDIX_C = os.path.join(BASE, "book", "14-附录C-版本历史与更新说明.md")
MARK_FILE = os.path.join(BASE, ".last-update.json")

def bump_version(current, patch_only=True):
    parts = current.split(".")
    if patch_only and len(parts) == 3:
        parts[2] = str(int(parts[2]) + 1)
    else:
        parts[-1] = str(int(parts[-1]) + 1)
    return ".".join(parts)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True, help="更新标题，如 v1.0.1 每周更新")
    ap.add_argument("--notes", required=True, help="更新说明（多行，每行一个要点）")
    ap.add_argument("--version", default=None, help="显式指定新版本号（缺省 patch+1）")
    ap.add_argument("--force", action="store_true", help="忽略同日去重，强制执行")
    args = ap.parse_args()

    # 幂等检查
    today = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(MARK_FILE):
        with open(MARK_FILE) as f:
            last = json.load(f)
        if last.get("date") == today and not args.force:
            print(f"今天({today})已执行过更新，跳过（--force 可强制执行）")
            return

    old_version = open(VERSION_FILE).read().strip()
    new_version = args.version or bump_version(old_version)
    today_cn = datetime.now().strftime("%Y-%m-%d")

    # 1. 写 VERSION
    open(VERSION_FILE, "w").write(new_version)

    # 2. CHANGELOG 头部插入
    entry = f"""## v{new_version} — {today_cn}

**{args.title}**

{args.notes}

---
"""
    with open(CHANGELOG) as f:
        content = f.read()
    # 插到第一个 ## 之前
    idx = content.find("## ")
    new_content = content[:idx] + entry + content[idx:]
    open(CHANGELOG, "w").write(new_content)

    # 3. 附录C 追加
    appendix_entry = f"""### v{new_version} — {today_cn}

**{args.title}**

{args.notes}

"""
    with open(APPENDIX_C, "a", encoding="utf-8") as f:
        f.write("\n" + appendix_entry)

    # 4. 重新生成 PDF（build_pdf.py 同时产出版本名 + 固定名，供 mkdocs 复制；英文版输出到 repo 根仅 GitHub 分发）
    subprocess.run([sys.executable, "tools/build_pdf.py", new_version], cwd=BASE, check=True, timeout=300)
    subprocess.run([sys.executable, "tools/build_pdf.py", new_version, "--lang", "en"], cwd=BASE, check=True, timeout=300)

    # 5. mkdocs build
    subprocess.run([os.path.join(BASE, ".venv", "bin", "mkdocs"), "build"], cwd=BASE, check=True, timeout=300)

    # 6. git commit + push
    subprocess.run(["git", "add", "-A"], cwd=BASE, check=True)
    subprocess.run(["git", "commit", "-m", f"v{new_version}: {args.title}"], cwd=BASE, check=True)
    push = subprocess.run(["git", "push", "origin", "main"], cwd=BASE, capture_output=True, text=True)
    if push.returncode != 0:
        print("WARN: git push 失败，稍后需手动推送：", push.stderr[-500:])
    else:
        print("git push OK")

    # 7. 完成标记
    with open(MARK_FILE, "w") as f:
        json.dump({"date": today, "version": new_version, "title": args.title}, f, ensure_ascii=False)

    print(f"✅ 更新完成：v{old_version} → v{new_version}")

if __name__ == "__main__":
    main()
