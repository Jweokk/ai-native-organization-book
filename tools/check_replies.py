#!/usr/bin/env python3
"""每日检查《AI 原生组织》宣传帖子的回复情况（通过 Airtap 云手机）。

检查目标：
- X 主帖: https://x.com/bobandersotayv/status/2091077591906103689
- Reddit r/artificial: https://www.reddit.com/r/artificial/s/EGXPsdLZLu

用法：
    python3 tools/check_replies.py [--timeout 600]

输出：Airtap agent 的文本报告（互动数 + 回复内容 + 审核状态）。
历史快照存 tools/replies_history.json（用于对比"较上次新增的回复"）。
"""
import json, os, subprocess, sys, time
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AIRTap_SKILL = os.path.expanduser("~/.hermes/skills/airtap")
HISTORY = os.path.join(BASE, "tools", "replies_history.json")

X_POST = "https://x.com/bobandersotayv/status/2091077591906103689"
REDDIT_POST = "https://www.reddit.com/r/artificial/s/EGXPsdLZLu"

def run(cmd, timeout=60):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return r.stdout

def create_task(message):
    out = run(["python3", "scripts/airtap.py", "task", "create",
               "--message", message, "--receiver-id", "cloud",
               "--model-id", "airtap-1.0"], timeout=90)
    try:
        return json.loads(out[out.index("{"):])["taskId"]
    except Exception:
        print("任务创建失败:", out[-300:])
        sys.exit(1)

def poll_task(task_id, timeout=600):
    deadline = time.time() + timeout
    while time.time() < deadline:
        out = run(["python3", "scripts/airtap.py", "task", "get-details",
                   "--task-id", task_id], timeout=90)
        try:
            d = json.loads(out[out.index("{"):])
        except Exception:
            time.sleep(15); continue
        state = d.get("taskState")
        if state in ("COMPLETED", "FAILED", "CANCELLED", "WAITING_FOR_USER_INTERVENTION"):
            return d
        time.sleep(20)
    return None

def agent_text(d):
    texts = []
    for m in d.get("messages", []):
        if m.get("type") == "agent":
            for p in m.get("parts", []):
                if p.get("type") == "text":
                    t = p["text"]
                    if len(t) > 30 and "Plan" not in t[:40]:
                        texts.append(t)
    return "\n".join(texts[-2:])

def main():
    timeout = 600
    if "--timeout" in sys.argv:
        timeout = int(sys.argv[sys.argv.index("--timeout") + 1])

    os.chdir(AIRTap_SKILL)

    instruction = f"""On this phone, check TWO pages:

PAGE 1 — in Chrome: visit {X_POST}
Read and report (use the Android accessibility tree / UI dump, NOT OCR):
(a) the reply count, repost/retweet count, and like count displayed on this post;
(b) the text of any replies visible under the post (first 2-3).

PAGE 2 — in the Reddit app (already logged in on this phone): find the post titled "I wrote a free open-source book on AI-native organizations — why 95% of AI projects fail and what the 5% do differently" in r/artificial.
- Open the Reddit app, tap the search icon, search for the title text, filter to the r/artificial community, open the matching post.
- Read and report (accessibility tree, NOT OCR):
(a) whether the post is visible normally, or shows 'removed' / 'awaiting moderator approval' / moderation messages;
(b) the comment count;
(c) the text of any visible comments (first 2-3).

Report everything as plain text with clear sections. If a page fails to load, say so.

IMPORTANT: Do NOT use CDP or the chrome-browser-automation skill. Operate purely visually with AutoPilot (tap, type, scroll). Use the current Chrome window; type URLs in the address bar."""

    print(f"⏳ 创建检查任务（{datetime.now().strftime('%H:%M')}）...")
    task_id = create_task(instruction)
    print(f"taskId: {task_id}")

    d = poll_task(task_id, timeout=timeout)
    if d is None:
        msg = "⚠️ 任务超时（poll 未完成），请手动检查云手机"
        print(msg)
        # 超时也写快照，避免 cron 运行丢记录
        snap = {"date": datetime.now().isoformat(), "task": "TIMEOUT", "report": msg}
        hist = []
        if os.path.exists(HISTORY):
            try:
                hist = json.load(open(HISTORY))
            except Exception:
                pass
        hist.append(snap)
        json.dump(hist[-60:], open(HISTORY, "w"), ensure_ascii=False, indent=1)
        sys.exit(0)

    state = d.get("taskState")
    print(f"状态: {state}")
    text = agent_text(d)
    if not text:
        text = "(agent 无文本输出，见截图)"
    print("=" * 60)
    print(text)
    print("=" * 60)

    # 历史快照
    snap = {"date": datetime.now().isoformat(), "task": state, "report": text[:3000]}
    hist = []
    if os.path.exists(HISTORY):
        try:
            hist = json.load(open(HISTORY))
        except Exception:
            pass
    hist.append(snap)
    json.dump(hist[-60:], open(HISTORY, "w"), ensure_ascii=False, indent=1)

    if state != "COMPLETED":
        print("⚠️ 任务未正常完成，结果可能不完整")

if __name__ == "__main__":
    main()
