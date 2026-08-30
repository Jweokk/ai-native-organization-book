"""mkdocs hooks：构建时把正文引用上标的相对 .md 链接重写为站内绝对路径。

源文件里上标链接是 GitHub 友好的相对形式（12-附录A-案例索引与资料出处.md#10-25），
mkdocs 不会重写内联 HTML 中的链接，这里手动重写为网站绝对路径（/12-附录A-案例索引与资料出处/#10-25）。
"""
import re

_PATTERN = re.compile(r'href="(12-附录A-案例索引与资料出处)\.md#([\d-]+)"')
_REPL = r'href="/\1/#\2"'


def on_page_content(html, page, config, files):
    return _PATTERN.sub(_REPL, html)
