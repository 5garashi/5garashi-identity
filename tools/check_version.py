"""
ファイル名 / File: tools/check_version.py
概要 / Description: 改版したファイルの版が VERSION と一致するか、本文の data-version がヘッダーの版と一致するかを確かめる。--stamp で書き込む(第12条 12-7 (6))
作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
作成日 / Created: 2026-10-12
ライセンス / License: MIT
SPDX-License-Identifier: MIT

使い方 / Usage:
    python tools/check_version.py                 # origin/main から変えたファイルを確かめる / check files changed since origin/main
    python tools/check_version.py --all           # 版の行があるすべてのファイルを一覧にして確かめる / list and check every file with a version line
    python tools/check_version.py --stamp FILE... # FILE の版を VERSION の値に書き換える / write VERSION into FILE

確かめること / Checks:
    (1) VERSION が3つの数字の1行であること
    (2) 変えたファイルにヘッダーの版の行(「版 / Version:」または「Version:」)があれば、VERSION と一致すること
    (3) data-version を付けた要素の番号が、そのファイルのヘッダーの版と一致すること
    (4) 内容を変えたのに VERSION が変わっていなければ注意を出す(誤字・体裁だけの直しなら上げなくてよい:12-7 (2))
"""

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
# ヘッダー(先頭の30行)にある版の行 / version line in the header (first 30 lines)
HEADER_RE = re.compile(r"^(\s*(?:版 / Version|Version):\s*)(\d+\.\d+(?:\.\d+)?)", re.M)
DATA_VERSION_RE = re.compile(r"(<[^<>]*\bdata-version\b[^<>]*>)(\d+\.\d+\.\d+)(</)")
HEADER_LINES = 30
SKIP_PREFIXES = ("old/", "backupDoc/", ".git/")


def read_version() -> str:
    v = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_RE.match(v):
        sys.exit(f"VERSION は 1.0.3 のような3つの数字にしてください / VERSION must be three numbers (got '{v}')")
    return v


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout


def changed_files() -> list:
    base = git("merge-base", "HEAD", "origin/main").strip() or "HEAD"
    names = set(git("diff", "--name-only", base).split())
    names |= set(git("ls-files", "--others", "--exclude-standard").split())
    return sorted(n for n in names if not n.startswith(SKIP_PREFIXES) and (ROOT / n).is_file())


def read_text(path: pathlib.Path):
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def header_version(text: str):
    head = "\n".join(text.splitlines()[:HEADER_LINES])
    m = HEADER_RE.search(head)
    return m.group(2) if m else None


def check_file(name: str, version: str, must_match: bool) -> list:
    text = read_text(ROOT / name)
    if text is None:
        return []
    errors = []
    hv = header_version(text)
    if must_match and hv is not None and hv != version:
        errors.append(f"{name}: ヘッダーの版 {hv} が VERSION {version} と違う / header {hv} differs from VERSION {version}")
    expected = hv or version
    for m in DATA_VERSION_RE.finditer(text):
        if m.group(2) != expected:
            errors.append(f"{name}: data-version {m.group(2)} がヘッダーの版 {expected} と違う / data-version {m.group(2)} differs from {expected}")
    return errors


def stamp(names: list, version: str) -> int:
    for name in names:
        path = ROOT / name if not pathlib.Path(name).is_absolute() else pathlib.Path(name)
        text = read_text(path)
        if text is None:
            print(f"{name}: 読めません / cannot read")
            continue
        lines = text.split("\n")
        head = "\n".join(lines[:HEADER_LINES])
        head = HEADER_RE.sub(lambda m: m.group(1) + version, head, count=1)
        text = "\n".join([head] + lines[HEADER_LINES:]) if len(lines) > HEADER_LINES else head
        text = DATA_VERSION_RE.sub(lambda m: m.group(1) + version + m.group(3), text)
        path.write_text(text, encoding="utf-8", newline="")
        print(f"{name}: {version} を書き込みました / stamped {version}")
    return 0


def main(argv: list) -> int:
    version = read_version()
    if argv[:1] == ["--stamp"]:
        return stamp(argv[1:], version)
    if argv[:1] == ["--all"]:
        names = [n for n in git("ls-files").split() if not n.startswith(SKIP_PREFIXES)]
        errors = []
        for n in names:
            text = read_text(ROOT / n)
            hv = header_version(text) if text else None
            if hv:
                print(f"  {hv:>8}  {n}")
            errors += check_file(n, version, must_match=False)
    else:
        names = changed_files()
        errors = []
        for n in names:
            errors += check_file(n, version, must_match=True)
        content_changed = [n for n in names if n not in ("VERSION", "CHANGELOG.md")]
        if content_changed and "VERSION" not in names:
            print("注意:内容を変えたのに VERSION が変わっていません。誤字・体裁だけの直しでなければ版を上げてください(12-7 (2))。")
            print("Note: content changed but VERSION did not. Raise it unless these are typo or formatting fixes only (12-7 (2)).")
    print(f"VERSION: {version}")
    for e in errors:
        print("  NG  " + e)
    if errors:
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
