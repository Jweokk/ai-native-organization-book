#!/usr/bin/env python3
"""引用一致性自检（每周更新完成后运行）。

检查三件事：
1. 附录 A 编号 vs 正文上标编号的差集（附录有条目但正文未引用 = 可能漏标）
2. 正文上标链接格式（必须是 <sup><a href="12-附录A-案例索引与资料出处.md#X-Y">[X-Y]</a></sup> 相对链接形式，不能是纯文本 sup 或绝对路径）
3. 正文引用的编号在附录 A 必须存在（悬空引用）

用法：
    python3 tools/check_refs.py
退出码：0 = 全部通过；1 = 有问题（输出明细）

注意：附录 A 收录全部来源，未标注上标的条目可能是"延伸阅读"（导语已说明），
因此差集只提示"建议人工确认"，不强制；链接格式与悬空引用是硬错误。
"""
import re, sys, glob, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPENDIX_ZH = os.path.join(BASE, "book", "12-附录A-案例索引与资料出处.md")
APPENDIX_EN = os.path.join(BASE, "book-en", "12-appendix-a-sources.md")
ZH_BODY = ["01-第1章-AI原生组织的崛起.md","02-第2章-什么是AI原生组织.md","03-第3章-证据-实证研究怎么看.md",
           "04-第4章-组织形态重构.md","05-第5章-工作流与决策重构.md","06-第6章-激励与人才.md",
           "07-第7章-案例集.md","09-第9章-挑战风险与未来.md","10-第10章-行业篇.md"]
EN_BODY = ["01-ch1-the-rise-of-ai-native-organizations.md","02-ch2-what-is-an-ai-native-organization.md",
           "03-ch3-the-evidence.md","04-ch4-rebuilding-organizational-structure.md",
           "05-ch5-redesigning-workflows-and-decisions.md","06-ch6-incentives-and-talent.md",
           "07-ch7-case-studies.md","09-ch9-challenges-risks-and-the-future.md","10-ch10-industry-guide.md"]


def read(path):
    return open(path, encoding="utf-8").read()


def main():
    errors = []      # 硬错误
    warnings = []    # 建议人工确认

    appendix_zh = read(APPENDIX_ZH)
    appendix_refs = set(re.findall(r'<a id="([\d-]+)"', appendix_zh))

    # 中英正文收集
    zh_body = "".join(read(os.path.join(BASE, "book", f)) for f in ZH_BODY)
    en_body = "".join(read(os.path.join(BASE, "book-en", f)) for f in EN_BODY)

    # 1. 上标链接格式（硬错误）
    for lang, body in [("中文", zh_body), ("英文", en_body)]:
        # 纯文本 sup（无链接）
        plain = re.findall(r'<sup>\[([\d-]+)\]</sup>(?!<a)', body)
        if plain:
            errors.append(f"[{lang}] 纯文本上标（缺链接）: {sorted(set(plain))[:5]}")
        # 绝对路径链接（GitHub 会坏）
        abslink = re.findall(r'<sup><a href="/12-[^"]*#([\d-]+)">', body)
        if abslink:
            errors.append(f"[{lang}] 绝对路径链接（GitHub 会坏）: {sorted(set(abslink))[:5]}")
        # 链接 href 形式检查
        bad_href = re.findall(r'<sup><a href="([^"]*)"', body)
        ok_zh = re.findall(r'<sup><a href="12-附录A-案例索引与资料出处\.md#[\d-]+">', body)
        ok_en = re.findall(r'<sup><a href="12-appendix-a-sources\.md#[\d-]+">', body)
        if lang == "中文" and len(ok_zh) != len(bad_href):
            errors.append(f"[中文] 存在非标准 href（应为 12-附录A-案例索引与资料出处.md#X-Y）: {len(bad_href)-len(ok_zh)} 处")
        if lang == "英文" and len(ok_en) != len(bad_href):
            errors.append(f"[英文] 存在非标准 href（应为 12-appendix-a-sources.md#X-Y）: {len(bad_href)-len(ok_en)} 处")

    # 2. 悬空引用（正文引用了附录不存在的编号 = 硬错误）
    zh_refs = set(re.findall(r'<sup><a href="12-附录A-案例索引与资料出处\.md#([\d-]+)">', zh_body)) | set(re.findall(r'<sup>\[([\d-]+)\]</sup>', zh_body))
    en_refs = set(re.findall(r'<sup><a href="12-appendix-a-sources\.md#([\d-]+)">', en_body)) | set(re.findall(r'<sup>\[([\d-]+)\]</sup>', en_body))
    for lang, refs in [("中文", zh_refs), ("英文", en_refs)]:
        missing = sorted(r for r in refs if r not in appendix_refs)
        if missing:
            errors.append(f"[{lang}] 悬空引用（附录A无此编号）: {missing[:10]}")

    # 3. 附录有条目正文未引用（警告，需人工确认是否漏标/延伸阅读）
    used = zh_refs | en_refs
    unused = sorted(appendix_refs - used)
    if unused:
        warnings.append(f"附录 A 有条目正文未标注 ({len(unused)} 条): {unused[:15]}{'...' if len(unused) > 15 else ''}")

    # 输出
    print("=" * 60)
    print("引用一致性自检")
    print(f"附录 A 条目: {len(appendix_refs)} | 中文正文引用: {len(zh_refs)} | 英文正文引用: {len(en_refs)}")
    print("=" * 60)
    if errors:
        for e in errors:
            print(f"❌ {e}")
    if warnings:
        for w in warnings:
            print(f"⚠️ {w}")
    if not errors and not warnings:
        print("✅ 全部通过")
    print()
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
