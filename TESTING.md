<!--
  ファイル名 / File: TESTING.md
  概要 / Description: Identityの文書と配布物の確認方法
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-11-05
  版 / Version: 4.23.0
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 確認方法

確認の共通基準は[品質確認規定](https://5garashi.github.io/5garashi-quality/)を参照する。本書にはIdentity固有の手順を記す。

- 本文変更：日英の意味、項番号、参照先、VERSION・表紙・ヘッダー・CHANGELOGを照合する。
- 翻訳変更：追加・変更した原文と訳文を共通のレビュー手順で別AIに見てもらい、判断を記録する。
- 配布物：python tools/build_standalone.pyで単一ファイル版を生成し、追加文がWeb版・単一ファイル版の双方に含まれることを確認する。
- 版：python tools/check_version.py、git diff --checkを実行する。変更していない文書の版は維持する。
- 表示：公開後、日英の追加項と版番号を確認する。表示の目視・狭い幅など未実施の項目は明記する。

## 4.23.0の確認記録

- 原稿：8-2の日英各1か所に(6)を追加し、既存(1)〜(5)の順序を保持したことを検証。
- 版・配布物：check_version.py、git diff --check、build_standalone.pyを実行。Web版と単一ファイル版の追加文・版を照合。
- 別AIレビュー：Copilotが回答。指示対象の曖昧さ、否定の英訳、重複を避ける説明の対象、主張の成立条件の明示という4点を修正した。「限定的な可能性」を「まれな例外」に替える提案は、限定の範囲と発生頻度が異なるため採用しなかった。
- 公開後の版・追加文・Release・配布状況は公開後に確認する。
- 表示の目視、320px幅、拡大、読み上げ、印刷は未実施。今回は文言の追加であり、CSS・操作は変更していない。表示全項目への適合を宣言しない。
