#!/usr/bin/env python3
"""生成《AI 原生组织》整本 PDF（中英双语）。

流程：book/*.md (按文件名排序) → python-markdown → HTML → weasyprint → PDF
验证：pdftotext 检查页数与非空。

用法：
    .venv/bin/python tools/build_pdf.py [版本号] [--lang zh|en]
    版本号缺省从 VERSION 文件读取。
    --lang en 生成英文版：读取 book-en/，输出到 repo 根目录（仅 GitHub 分发，不进域名站点）。
"""
import sys, os, re, glob, subprocess, shutil
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGS = {
    "zh": {
        "dir": "book",
        "out": "book",      # docs_dir 内，mkdocs 自动复制到 site/（域名站点）
        "fname": "ai-native-organization",
        "title": "AI 原生组织",
        "subtitle": "AI-Native Organization：让组织长出 AI 基因",
        "meta": "Jweokk 著 · {today} · v{version}",
        "blurb": "模型已经不稀缺了，能把模型长进组织里的人，才稀缺。<br>从 95% 的项目失败率，到 DeepSeek 160 人的创新密度——<br>这本书讲清楚：什么是 AI 原生组织，证据怎么说，以及怎么打造。",
        "disclaimer": "本书著作权归作者 Jweokk 所有，免费阅读与非商业性分享，商业用途须事先获得书面许可。<br>联系方式：weokk2025@gmail.com",
        "font": '"WenQuanYi Zen Hei", "Noto Sans CJK SC", "Source Han Sans CN", sans-serif',
        "toc_title": "目录",
    },
    "en": {
        "dir": "book-en",
        "out": ".",         # repo 根目录，仅 GitHub 分发（域名只面向中文读者）
        "fname": "ai-native-organization-en",
        "title": "AI-Native Organization",
        "subtitle": "Growing AI into the Organization's DNA",
        "meta": "Jweokk · {today} · v{version}",
        "blurb": "Models are no longer scarce. People who can grow models into their organizations are.<br>From the 95% project failure rate to DeepSeek's 160-person innovation density —<br>this book explains what an AI-native organization is, what the evidence says, and how to build one.",
        "disclaimer": "Copyright © Jweokk. Free for reading and non-commercial sharing; commercial use requires prior written permission.<br>Contact: weokk2025@gmail.com",
        "font": '"DejaVu Sans", "Noto Sans", sans-serif',
        "toc_title": "Contents",
    },
}

def read_version():
    vf = os.path.join(BASE, "VERSION")
    if os.path.exists(vf):
        return open(vf).read().strip()
    return "1.0.0"

def md_to_html(md_text):
    import markdown
    return markdown.markdown(md_text, extensions=["tables", "toc", "admonition", "fenced_code", "footnotes"])

def chapter_files(book_dir):
    fs = sorted(glob.glob(os.path.join(book_dir, "*.md")))
    # index.md 是站点首页、README.md 是仓库说明，均不进 PDF
    return [f for f in fs if os.path.basename(f) not in ("index.md", "README.md")]

def build():
    lang = "en" if "--lang" in sys.argv and sys.argv[sys.argv.index("--lang") + 1] == "en" else "zh"
    L = LANGS[lang]
    book_dir = os.path.join(BASE, L["dir"])
    out_dir = os.path.join(BASE, L["out"])
    version = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "--lang" else read_version()
    today = datetime.now().strftime("%Y-%m-%d") if lang == "en" else datetime.now().strftime("%Y年%m月%d日")

    # 收集章节
    chapters = []
    for f in chapter_files(book_dir):
        name = os.path.basename(f)
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
        m = re.search(r"^#\s+(.+)$", text, flags=re.M)
        title = m.group(1).strip() if m else name
        body = md_to_html(text)
        chapters.append((title, body))

    # TOC
    toc_items = "".join(
        f'<p class="toc-entry"><span class="toc-num">{i+1:02d}</span>{t}</p>'
        for i, (t, _) in enumerate(chapters)
    )

    # 正文
    body_html = ""
    for i, (title, body) in enumerate(chapters):
        body_html += f'<h2 class="chapter-title" id="ch{i+1}">{title}</h2>\n{body}\n'

    meta = L["meta"].format(today=today, version=version)
    font = L["font"]

    html = f"""<!DOCTYPE html>
<html lang="{'en' if lang == 'en' else 'zh-CN'}">
<head>
<meta charset="utf-8">
<style>
  @page {{
    size: letter;
    margin: 2.2cm 2.5cm 2.2cm 2.5cm;
    @bottom-center {{
      content: counter(page);
      font-family: {font};
      font-size: 9pt;
      color: #999;
    }}
  }}
  @page:first {{
    @bottom-center {{ content: none; }}
  }}
  body {{
    font-family: {font};
    font-size: 10.5pt;
    line-height: 1.75;
    color: #222;
    text-align: justify;
    orphans: 3;
    widows: 3;
  }}
  .cover {{
    page-break-after: always;
    background: #1a237e;
    color: white;
    padding: 4cm 1.5cm 2cm 1.5cm;
    margin: -2.2cm -2.5cm;
    width: 21.6cm;
    height: 27.94cm;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}
  .cover h1 {{
    font-size: 28pt;
    font-weight: 700;
    text-align: center;
    margin-bottom: 8pt;
    letter-spacing: 3pt;
  }}
  .cover .subtitle {{
    font-size: 13pt;
    text-align: center;
    color: #ccc;
    margin-bottom: 2cm;
  }}
  .cover .meta {{
    font-size: 10pt;
    text-align: center;
    color: #aaa;
    margin-bottom: 1cm;
  }}
  .cover .blurb {{
    font-size: 10pt;
    text-align: center;
    color: #bbb;
    line-height: 1.6;
    max-width: 14cm;
    margin: 1.5cm auto;
  }}
  .cover .disclaimer {{
    font-size: 7.5pt;
    text-align: center;
    color: #888;
    margin-top: auto;
  }}
  .toc-page {{
    page-break-after: always;
  }}
  .toc-page h2 {{
    font-size: 18pt;
    color: #1a237e;
    border-bottom: 2px solid #1a237e;
    padding-bottom: 6pt;
    margin-bottom: 14pt;
  }}
  .toc-entry {{
    font-size: 11pt;
    line-height: 2;
    margin: 0;
  }}
  .toc-num {{
    font-weight: 700;
    color: #1a237e;
    margin-right: 8pt;
  }}
  .chapter-title {{
    font-size: 16pt;
    color: #1a237e;
    border-bottom: 1.5px solid #b0bec5;
    padding-bottom: 4pt;
    margin-top: 18pt;
    margin-bottom: 12pt;
    page-break-before: always;
  }}
  h1 {{
    font-size: 15pt;
    color: #1a237e;
    margin-top: 18pt;
  }}
  h2 {{
    font-size: 13pt;
    color: #333;
    margin-top: 14pt;
  }}
  h3 {{
    font-size: 11.5pt;
    color: #444;
  }}
  p {{
    text-indent: 2em;
    margin: 6pt 0;
  }}
  li {{ margin: 3pt 0; }}
  table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 9.5pt;
    margin: 10pt 0;
  }}
  th, td {{
    border: 1px solid #b0bec5;
    padding: 5pt 7pt;
    text-align: left;
  }}
  th {{ background: #e8eaf6; }}
  blockquote {{
    border-left: 3px solid #1a237e;
    margin: 8pt 0;
    padding: 4pt 12pt;
    color: #555;
    background: #f5f5f5;
  }}
  code {{
    font-family: "DejaVu Sans Mono", monospace;
    font-size: 9pt;
    background: #f0f0f0;
    padding: 1pt 3pt;
  }}
  pre {{
    background: #f7f7f7;
    border: 1px solid #ddd;
    padding: 8pt;
    font-size: 9pt;
    white-space: pre-wrap;
  }}
  a {{ color: #1a237e; text-decoration: none; }}
  /* PDF 中显示链接完整 URL——仅限外部 http 链接（致谢与附录出处）；锚点引用链接(#ref)不显示 */
  a[href^="http"]::after {{ content: " (" attr(href) ")"; font-size: 8pt; color: #666; }}
  /* 引用上标样式 */
  sup {{ font-size: 6.5pt; color: #1a237e; vertical-align: super; }}
  .footnote {{ font-size: 8.5pt; color: #666; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 14pt 0; }}
</style>
</head>
<body>
  <div class="cover">
    <h1>{L['title']}</h1>
    <div class="subtitle">{L['subtitle']}</div>
    <div class="meta">{meta}</div>
    <div class="blurb">
      {L['blurb']}
    </div>
    <div class="disclaimer">
      {L['disclaimer']}
    </div>
  </div>
  <div class="toc-page">
    <h2>{L['toc_title']}</h2>
    {toc_items}
  </div>
  {body_html}
</body>
</html>
"""
    os.makedirs(out_dir, exist_ok=True)
    pdf_path = os.path.join(out_dir, f"{L['fname']}-v{version}.pdf")
    fixed_path = os.path.join(out_dir, f"{L['fname']}.pdf")

    import weasyprint
    weasyprint.HTML(string=html).write_pdf(pdf_path)
    shutil.copy(pdf_path, fixed_path)

    # 验证
    txt = subprocess.run(["pdftotext", fixed_path, "-"], capture_output=True, text=True).stdout
    pages = len(txt.split("\f")) - 1 if txt else 0
    nonempty = len(txt.strip()) > 2000
    garbled = txt.count("□") + txt.count("�") > 5
    print(f"PDF({lang}): {pdf_path}")
    print(f"pages={pages} text_chars={len(txt.strip())} nonempty={nonempty} garbled={garbled}")
    if pages < 20 or not nonempty or garbled:
        sys.exit("验证失败：PDF 异常")
    return pdf_path

if __name__ == "__main__":
    build()
