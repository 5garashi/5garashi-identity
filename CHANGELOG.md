# 改版履歴 / Changelog — 5garashi.com設計事務所 Design Office Identity

アイデンティティ運用仕様の改版履歴。第8条 8-5 に従い、版番号・更新日・変更内容で管理する。新しい版を上に書く。
Revision history of the Identity Operating Rules, managed by version, date, and changes (Art. 8-5). Newest first.

## v4.7 — 2026-10-08

外部レビュー(複数AIによる分析、2026-10-08)を反映。
External review (multi-AI analysis, 2026-10-08) applied.

### ページの構成 / Page structure
- Web版 `index.html` は、オリジナル版PNGとテーマ曲MP3を `assets/` から読み込む形に変更(約2.55MB → 約0.2MB)。音源は再生時にだけ読み込む(`preload="none"`)。
  The web edition loads the original PNG and theme MP3 from `assets/` (about 2.55MB → 0.2MB); audio loads only on play.
- 全部入りの単一ファイル版 `5garashi_identity_v4_7.html` は `tools/build_standalone.py` で `index.html` から生成する形に変更。直接編集しない。
  The all-in-one edition is now generated from `index.html` by `tools/build_standalone.py`; do not edit it directly.
- オリジナル版マークを `assets/5garashi_mark_original.png` として書き出し(これまではHTML内にのみ存在)。
  Original mark exported to `assets/5garashi_mark_original.png` (previously only inside the HTML).
- 改版履歴をHTMLコメントから本ファイルへ移し、本文の目次直後に「本版の変更点」を表示。
  Revision history moved from an HTML comment to this file; a visible "What's new" block follows the table of contents.

### 検索・共有 / Search and sharing
- ページ概要(meta description)、OGP、Twitterカード、正規URL(canonical)、言語別URL(hreflang)を追加。共有用画像 `assets/og_image.png`(1200×630、`tools/og_image.html` から生成)を追加。
  Added meta description, Open Graph, Twitter card, canonical, and hreflang; added `assets/og_image.png`.
- `?lang=en` で英語版を直接開けるようにし、切り替えボタンを押すとURLにも反映する。`html lang` は切替時に `ja`/`en` に変わる(v4.6 から対応済みを確認)。
  `?lang=en` opens the English edition directly and the toggle updates the URL. `html lang` switches between `ja` and `en` (already the case in v4.6; confirmed).
- 英語表示のときは canonical と og:url を `?lang=en`、og:locale を `en_US` に切り替え、hreflang と食い違わないようにした。
  In English view, canonical and og:url switch to `?lang=en` and og:locale to `en_US`, consistent with hreflang.

### 本文 / Content
- 表紙:事務所の紹介、名前の読み方、公式サイトへのリンクを追加。
  Cover: office introduction, pronunciation, and official site link.
- 第2条 2-2:ink地のpaper抜きのコントラスト比を 6.7:1 から実測値 7.14:1 に訂正(6.66:1 は head × ink の値)。
  Art. 2-2: paper-on-ink contrast corrected from 6.7:1 to the measured 7.14:1.
- 第6条:Windowsでの代替書体(Yu Gothic → Meiryo)を明記し、CSSに Meiryo を追加。
  Art. 6: Windows fallback (Yu Gothic, then Meiryo) stated and added to the CSS.
- 第6条:本書自体が「意味を持つ注記は12px以上」に違反していた箇所(禁止事項の説明、色見本の名称、判定ラベル、表紙の日付、フッターなど)を12pxに引き上げ。11pxは装飾的ラベル(条見出しの副題、色見本の札、対照表の見本文字)だけに残した。
  Art. 6: this document's own violations of "meaningful notes 12px or larger" raised to 12px; 11px remains only on decorative labels.
- 第5条:区切り線の見本で、横倒しの唐辛子3本が重なって1本に見えていた表示不具合を修正。
  Art. 5: fixed the divider sample, where the three sideways chilis overlapped and looked like one line.
- 第7条 7-1:CSSで使用中なのに表になかった8組(ink × card、volt-deep × card、volt-deep × head、steel × head、ok × card、ok × paper、cream × ok、volt × card)を追加。AAAを必須とする範囲(本文の基本組のみ)を明記。確認日と計算方法を表に添え、`tools/check_contrast.py` を追加。volt × ink(1.31:1)を直接重ねることを禁止し、第10条にも追加。
  Art. 7-1: eight pairs already used in the CSS added to the table; AAA scope clarified; check date and method recorded; `tools/check_contrast.py` added; volt on ink (1.31:1) prohibited, also listed in Art. 10.
- 第7条 7-7:出荷前チェックに (d) 画面幅320pxのリフロー(WCAG 2.2 達成基準 1.4.10)と、確認結果の記録を追加。本書自体の320px表示での横はみ出し(シンボルマーク欄・コントラスト表)を修正。
  Art. 7-7: added (d) 320px reflow (WCAG 2.2 SC 1.4.10) and a record-keeping rule; fixed this document's own overflow at 320px.
- 第8条:8-7 文例(問い合わせへの返信・エラー表示・報告書の書き出しの良い例と悪い例)と、8-8 確かさを表す語(確認済み・推定・仮定・可能性がある・未確認)の定義を追加。
  Art. 8: added 8-7 do/don't examples and 8-8 definitions of certainty terms.
- 第12条:12-3 の配布構成を実在するファイルに合わせて更新し、`tools/` を追記。12-4 早見表、12-5 問い合わせ先を追加。12-5 では、事前の問い合わせが要る場合を「改変版を使う」「名称・ロゴを自分の商品やサービス、共同発表に使う」に絞り、根拠(CC BY-ND 4.0 と 12-2 の権利留保)を明記した。
  Art. 12: package list matched to actual files, with `tools/` added; added 12-4 at-a-glance summary and 12-5 contact, which names when an inquiry is needed and on what basis (CC BY-ND 4.0 and the rights reserved in 12-2).

### アセット / Assets
- 英語白黒ロゴタイプの編集用原本 `assets/5garashi_logotype_en_bw.svg` を追加(英語カラー編集用原本の配置のまま、日本語白黒と同じくスミ #1A1A1A・白地に置き換え)。
  Added the EN monochrome editing master, derived from the EN color master with the same black #1A1A1A / white treatment as the JA monochrome master.
- `5garashi_logotype_en.svg` と `5garashi_logotype_bw_outlined_no_box.svg` のヘッダーのファイル名・概要の誤記を訂正。
  Corrected wrong file names and descriptions in the headers of two SVGs.

## v4.6 — 2026-07-12
- 公式ロゴ表示をCSS文字組みから日英・カラー/白黒のアウトラインSVGへ移行。表紙、第3条、第9条を同一公式データに統一し、単一HTMLへ内蔵。SVGのviewBox統一・空text要素除去・配布構成更新を実施。
  Official logotypes migrated from CSS-built text to outlined SVGs in JA/EN and color/monochrome; cover, Art. 3, and Art. 9 now share the same official data embedded in the single HTML; SVG viewBoxes normalized, empty text remnants removed, distribution list updated.

## v4.5 — 2026-07-11
- 第8条を全面改訂:文章構成、断定と責任、技術文書での絵文字、ファイル名・タイトル・説明文の命名、二言語表記を規定。「完全版」「最終版」「最終整理」を原則不使用とし、版番号・更新日・対象範囲による管理へ統一。
  Art. 8 fully revised: structure, certainty and responsibility, emoji in technical documents, naming of files/titles/descriptions, and bilingual wording; completion labels replaced by objective version, date, and scope identifiers.

## v4.4 — 2026-07-11
- 「間」に「余白に語らせる」を追記。手すりの句に「進化させ続けるもの」を追記。「グランドルール」の語を全廃(運用仕様へ改称・第2条の当該文を削除)。第8条を5語の人格と接続した構成(8-1 声の性格/8-2 文体の原則)に改善。
  "Ma" now ends with "let the empty space do the talking"; the handrail phrase gains "made to evolve"; the term "ground rules" retired throughout (renamed to operating rules; sentence removed from Art. 2); Art. 8 restructured around the five-word voice (8-1 voice, 8-2 principles).

## v4.3 — 2026-07-11
- 外部レビュー反映:版表記統一。ライセンスをCC BY-ND 4.0に再設定(第12条新設:特記MIT断片・誤認防止・配布構成)。WCAG 2.2 AAへ更新し適用範囲を区分。文書自身の規定違反を解消(表紙の影・モック化・掲載例外・縦組み規定・停止手段)。文字サイズ規定の矛盾解消。cream #FFF3D6を正式登録。原本2系統(編集用/アウトライン配布用)。lang属性付与・印刷CSS・reduced-motion対応を拡充。
  External review applied: version strings unified; license reset to CC BY-ND 4.0 (new Art. 12); WCAG 2.2 AA with scoped applicability; self-violations fixed (cover shadow, mockup, example exemption, vertical rule, halt control); font-size rule contradiction resolved; cream #FFF3D6 registered; dual masters (editing/outlined); lang attributes, print CSS, expanded reduced-motion support.

## v4.2 — 2026-07-11
- ブランドの人格を5語に拡張(5語目「調和」=4語を横から貫き際立たせる)。SVG原本一式を公式アセットとして規定。テーマ曲の編集用原本 5garashi_theme.mid(MIDI)を追加。
  Personality expanded to five words (the fifth, "Harmony", crosses and balances the other four); SVG master set defined as official assets; editable theme source 5garashi_theme.mid (MIDI) added.

## v4.1 — 2026-07-11
- 第1条を概念的に抽象化(サービス列挙を廃し「深さと近さ」へ)。表紙文言を「創作物が醸成するオフィスアイデンティティ」に変更。第11条に楽譜を追加、曲名を「五辛子(ごがらし)のテーマ」に改称。オリジナル版ロゴをPNG原寸に復元。
  Art. 1 abstracted (service lists replaced by "depth and nearness"); cover wording now "the office identity every creation cultivates"; musical score added to Art. 11 and theme renamed "Gogarashi no Theme"; original mark restored to full-resolution PNG.

## v4.0 — 2026-07-11
- 公式サイト・運用ルールの全体像を反映:二本柱(設計部門×まちのデジタル便利屋さん)と適用範囲(基板・画面・紙・音)を第1条に明記。和の意匠を導入(和の心/正の字/間/伝統色の和名/五行)。9-5 README署名を追加。合言葉を改訂。
  Full scope from the website and operating rules reflected: two pillars and all surfaces (board, screen, paper, sound) in Art. 1; Japanese aesthetics added (wa spirit, the character 正, ma, traditional color names, five elements); 9-5 README signature; motto revised.

## v3.3 — 2026-07-11
- 表紙タイトルを第3条ロゴタイプに変更。英語版ロゴタイプ2行目を「Design Office」に。3-6モノクロ(白黒)文書規定を新設。テーマ曲5拍目を低音マリンバ(2オクターブ下・金属的倍音除去)に変更。
  Cover title now uses the Art. 3 logotype; EN logotype line 2 reads "Design Office"; new 3-6 monochrome rules; theme beat-5 lowered two octaves to bass marimba, metallic partials removed.

## v3.2 — 2026-07-11
- シンプル版を基本マークに昇格(表紙をシンプル版に変更)。テーマ曲の5拍目を金属ベルから木琴(マリンバ)音色に変更。
  Simple mark promoted to primary (cover updated); theme beat-5 changed from metal bell to marimba (wooden) tone.

## v3.1 — 2026-07-11
- テーマ曲改訂:5拍目アクセントをソフトベル(まろやかな長い余韻)に変更。
  Theme revised: beat-5 accent changed to a soft bell with a long, mellow resonance.

## v3 — 2026-07-11
- 日英バイリンガル化(切替ボタン)・第11条サウンドアイデンティティ新設(テーマ曲MP3内蔵)。
  Bilingual JA/EN toggle; Art. 11 Sound Identity added (theme MP3 embedded).

## v2 — 2026-07-11
- シンボルマーク2種公認・第7条UD新設。
  Two symbol marks approved; Art. 7 Universal Design added.

## v1 — 2026-07-11
- 初版。
  First edition.

---

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office
**最終更新 / Last updated**: 2026-10-08 JST
