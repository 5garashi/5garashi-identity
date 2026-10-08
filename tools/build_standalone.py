"""
ファイル名 / File: tools/build_standalone.py
概要 / Description: Web版 index.html から、画像と音源を内蔵した単一ファイル版 5garashi_identity_vX_Y.html を生成する(第12条 12-3)
作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
作成日 / Created: 2026-10-08
ライセンス / License: MIT
SPDX-License-Identifier: MIT

使い方 / Usage:
    python tools/build_standalone.py
"""

import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 内蔵するアセット(index.html 内の参照, MIMEタイプ)/ Assets to embed (reference in index.html, MIME type)
EMBED = [
    ("assets/5garashi_mark_original.png", "image/png"),
    ("assets/5garashi_theme.mp3", "audio/mpeg"),
]


def main() -> int:
    src = (ROOT / "index.html").read_text(encoding="utf-8")

    m = re.search(r"版 / Version: (\d+)\.(\d+)", src)
    if not m:
        print("index.html のヘッダーに「版 / Version: X.Y」が見つかりません", file=sys.stderr)
        return 1
    out_name = f"5garashi_identity_v{m.group(1)}_{m.group(2)}.html"

    for rel, mime in EMBED:
        ref = f'src="{rel}"'
        if src.count(ref) != 1:
            print(f"{ref} が index.html に1回だけ現れる必要があります", file=sys.stderr)
            return 1
        data = base64.b64encode((ROOT / rel).read_bytes()).decode("ascii")
        src = src.replace(ref, f'src="data:{mime};base64,{data}"')

    src = re.sub(
        r"ファイル名 / File: index\.html[^\n]*",
        f"ファイル名 / File: {out_name}(単一ファイル版。index.html から tools/build_standalone.py で生成。直接編集しない)",
        src,
        count=1,
    )

    out = ROOT / out_name
    out.write_text(src, encoding="utf-8", newline="")
    print(f"{out_name}: {out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
