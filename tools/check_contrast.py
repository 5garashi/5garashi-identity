"""
ファイル名 / File: tools/check_contrast.py
概要 / Description: 公式パレット(昼・夜)の文字色×背景色のコントラスト比を WCAG 2.2 の相対輝度式で計算する(第7条 7-1 の実測表の根拠)
作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
作成日 / Created: 2026-10-08
最終更新 / Last updated: 2026-10-11
ライセンス / License: MIT
SPDX-License-Identifier: MIT

使い方 / Usage:
    python tools/check_contrast.py
"""

# 昼の配色(第4条)/ Day palette (Art. 4)
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

# 夜の配色(第4条 4-2)。変数名は昼と同じ / Night palette (Art. 4-2), same variable names
NIGHT = {
    "paper": "#1A2212",
    "head": "#2B3A20",
    "ink": "#EFE6C4",
    "steel": "#D9B98C",
    "volt": "#F07B5F",
    "volt-deep": "#F7A58E",
    "card": "#222C1A",
    "line": "#4C5C3B",
    "ok": "#9FCC7E",
    "cream": "#1A2212",
    "mark": "#ADADA5",
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

# 夜の配色で使用を認める組み合わせ(第7条 7-1「夜の配色」)
# Pairs approved for the night palette (Art. 7-1, night table)
NIGHT_APPROVED = [
    ("ink", "paper", False),
    ("ink", "card", False),
    ("ink", "head", False),
    ("steel", "paper", False),
    ("steel", "card", False),
    ("steel", "head", False),
    ("volt-deep", "paper", False),
    ("volt-deep", "card", False),
    ("volt-deep", "head", False),
    ("volt", "paper", False),
    ("volt", "card", False),
    ("ok", "paper", False),
    ("ok", "card", False),
    ("head", "ink", False),
    ("cream", "volt", False),
    ("cream", "volt-deep", False),
    ("cream", "ok", False),
    ("mark", "paper", False),
    ("mark", "card", False),
    ("mark", "head", False),
]

# 文字・状態表示として直接重ねてはならない組み合わせ(第7条・第10条)
# Pairs that must never be layered as text or state indicators (Art. 7, Art. 10)
FORBIDDEN = [
    ("volt", "ink"),
]
NIGHT_FORBIDDEN = [
    ("volt", "ink"),
]

# 参考:昼の volt(マークの色)を夜の地に置いた場合。マークを灰色抜きにする根拠(第3条 3-7、第4条 4-2)
# Reference: the day volt (mark color) on night grounds — why the mark is reversed in dark mode (Art. 4-2)
NIGHT_MARK = [
    (PALETTE["volt"], "paper"),
    (PALETTE["volt"], "head"),
]


def _channel(c: int) -> float:
    s = c / 255
    return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def ratio_hex(fg: str, bg: str) -> float:
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def ratio(fg: str, bg: str, palette: dict = PALETTE) -> float:
    return ratio_hex(palette[fg], palette[bg])


def grade(r: float) -> str:
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA"
    if r >= 3:
        return "AA-large/non-text"
    return "FAIL"


def _report(title: str, pairs: list, palette: dict) -> int:
    failed = 0
    print(title)
    for fg, bg, bold in pairs:
        r = ratio(fg, bg, palette)
        note = " (bold only)" if bold else ""
        print(f"  {fg:>9} x {bg:<9} {r:5.2f}:1  {grade(r)}{note}")
        if r < 4.5:
            failed += 1
    return failed


def main() -> int:
    failed = _report("Approved pairs (day)", APPROVED, PALETTE)
    failed += _report("Approved pairs (night)", NIGHT_APPROVED, NIGHT)
    print("Forbidden pairs (day)")
    for fg, bg in FORBIDDEN:
        print(f"  {fg:>9} x {bg:<9} {ratio(fg, bg):5.2f}:1")
    print("Forbidden pairs (night)")
    for fg, bg in NIGHT_FORBIDDEN:
        print(f"  {fg:>9} x {bg:<9} {ratio(fg, bg, NIGHT):5.2f}:1")
    print("Reference: day volt mark on night grounds")
    for fg_hex, bg in NIGHT_MARK:
        print(f"  {fg_hex:>9} x {bg:<9} {ratio_hex(fg_hex, NIGHT[bg]):5.2f}:1")
    if failed:
        print(f"{failed} approved pair(s) below 4.5:1")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
