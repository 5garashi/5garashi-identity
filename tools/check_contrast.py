"""
ファイル名 / File: tools/check_contrast.py
概要 / Description: 公式パレットの文字色×背景色のコントラスト比を WCAG 2.2 の相対輝度式で計算する(第7条 7-1 の実測表の根拠)
作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
作成日 / Created: 2026-10-08
ライセンス / License: MIT
SPDX-License-Identifier: MIT

使い方 / Usage:
    python tools/check_contrast.py
"""

PALETTE = {
    "paper": "#F9EFCB",
    "head": "#FFE699",
    "ink": "#385723",
    "steel": "#7B4A21",
    "volt": "#B92613",
    "volt-deep": "#8C1B0D",
    "card": "#FFFDF2",
    "line": "#DFCF9A",
    "ok": "#3E6B2A",
    "cream": "#FFF3D6",
}

# 第7条 7-1 で使用を認める組み合わせ(文字色, 背景色, 太字のみか)
# Pairs approved in Art. 7-1 (text, background, bold-only)
APPROVED = [
    ("ink", "paper", False),
    ("ink", "card", False),
    ("ink", "head", False),
    ("steel", "card", False),
    ("steel", "paper", False),
    ("steel", "head", False),
    ("volt-deep", "paper", False),
    ("volt-deep", "card", False),
    ("volt-deep", "head", False),
    ("ok", "paper", False),
    ("ok", "card", False),
    ("head", "ink", False),
    ("cream", "volt-deep", False),
    ("cream", "volt", False),
    ("cream", "ok", False),
    ("volt", "paper", True),
    ("volt", "card", True),
]

# 文字・状態表示として直接重ねてはならない組み合わせ(第7条 7-2・第10条)
# Pairs that must never be layered as text or state indicators (Art. 7-2, Art. 10)
FORBIDDEN = [
    ("volt", "ink"),
]


def _channel(c: int) -> float:
    s = c / 255
    return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def ratio(fg: str, bg: str) -> float:
    a, b = luminance(PALETTE[fg]), luminance(PALETTE[bg])
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def grade(r: float) -> str:
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA"
    if r >= 3:
        return "AA-large/non-text"
    return "FAIL"


def main() -> int:
    failed = 0
    print("Approved pairs")
    for fg, bg, bold in APPROVED:
        r = ratio(fg, bg)
        g = grade(r)
        note = " (bold only)" if bold else ""
        print(f"  {fg:>9} x {bg:<9} {r:5.2f}:1  {g}{note}")
        if r < 4.5:
            failed += 1
    print("Forbidden pairs")
    for fg, bg in FORBIDDEN:
        print(f"  {fg:>9} x {bg:<9} {ratio(fg, bg):5.2f}:1")
    if failed:
        print(f"{failed} approved pair(s) below 4.5:1")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
