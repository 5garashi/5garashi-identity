# 改版履歴 / Changelog — 5garashi.com設計事務所 Design Office Identity

アイデンティティ運用仕様の改版履歴。第8条 8-5 に従い、版番号・更新日・変更内容で管理する。新しい版を上に書く。
Revision history of the Identity Operating Rules, managed by version, date, and changes (Art. 8-5). Newest first.

## 4.12.0 — 2026-10-12

本書も `VERSION` ファイルで版を管理する最初の版。見出しの番号はこの版から v を付けない(12-7 (9))。
The first version of this document managed by a `VERSION` file. Headings drop the "v" from this version on (12-7 (9)).

### 本文 / Content
- 第12条 12-7「版の管理(ソフトウェア・文書)」を新設(mdEditor で運用を始めた版の管理をもとに、文書にも広げた)。
  New Art. 12-7 "Versioning (software and documents)", based on the versioning adopted in mdEditor and widened to documents.
  - 対象は、1つのアプリまたは1組の文書を入れたフォルダー(ふつうは Git のリポジトリ1つ)で、一番上に `VERSION`(3つの数字)を置くもの。単独のフォルダーで管理していないもの、試作や作業用のスクリプト、この決まりより前の旧版・現行版は対象外。
    Scope: a folder holding one app or one set of documents with a three-number `VERSION` at its top; loose files, prototypes, and versions made before this rule are out of scope.
  - 版を上げるかは人または AI が判断する。内容(規定・数値・表示)が変わる変更は必ず上げ、誤字・体裁だけの直しは上げなくてよい。大きな変更は1つ目、追加・変更は2つ目、細かな直しは3つ目の数字。
    A person or an AI decides; content changes always raise it, typo and formatting fixes need not; major/minor/patch by the size of the change.
  - アプリなど読み取れるものは `VERSION` から読み取り、文書と静的な HTML は作成・改版のときに書き込む。文書に書く版は、その文書を最後に改版したときの版。
    Apps read `VERSION`; documents and static HTML have it written in when created or revised, and show the version of their last revision.
  - 版の番号を書く場所は少なくし、本文では表紙など1か所に限って、ほかは「本版」と書く。HTML の本文の番号は `data-version` を付けた要素に入れる。`tools/check_version.py` で確かめる。
    Write the number in few places: one place in the body at most, "this version" elsewhere; HTML numbers go in `data-version` elements; `tools/check_version.py` checks them.
  - README の版の行(ソフトウェア)、CHANGELOG の見出し(`## 1.0.3 — YYYY-MM-DD`、v なし。以前の v ありの見出しもワークフローは読む)、main で `VERSION` が変わったときのタグ `vX.Y.Z` と GitHub の Release、1つのファイルのツール、タグと公開日の関係を定めた。
    README version line, CHANGELOG headings, tags and Releases on `VERSION` changes, single-file tools, and tags versus release dates defined.
- 9-3 (4):`VERSION` をヘッダーの対象外に追加。9-3 (6):版の行の決まり(文書は最後に改版したときの `VERSION`、1つのファイルのツールはこの行が正、`VERSION` を読み取るソースコードには書かない)。
  9-3 (4) exempts `VERSION`; 9-3 (6) is the version-line rule.
- 8-5 から 12-7 を参照。9-5:ソフトウェアの README の冒頭に版の行。12-6:配布物に CHANGELOG.md を追加。
  8-5 points to 12-7; 9-5 README version line; 12-6 adds CHANGELOG.md.

### 本書への当てはめ / Applied to this document
- `VERSION` を追加し、本版を 4.12.0 とした。本文に書く版の番号は表紙だけにし(`data-version`)、タイトル・OGP・ページ概要・フッター・本版の変更点・JavaScript のタイトルからは除いた。ヘッダーの「版 / Version」は 4.12.0。
  `VERSION` added (4.12.0). The number now appears in the body only on the cover; removed from the title, OGP, description, footer, and script titles.
- 単一ファイル版のファイル名は `VERSION` から付ける(`5garashi_identity_v4_12_0.html`)。`tools/build_standalone.py` を変更。
  The single-file edition's name comes from `VERSION`; `tools/build_standalone.py` updated.
- `tools/check_version.py` を追加(変えたファイルの版と `VERSION` の一致、`data-version` とヘッダーの一致、`--stamp` での書き込み)。
  `tools/check_version.py` added.
- `.github/workflows/release.yml` を追加。main で `VERSION` が変わったら、タグ `v4.12.0` と Release を作る。
  `.github/workflows/release.yml` added: tags and releases when `VERSION` changes on main.
- `assets/README.md` に 9-3 のヘッダーを付け、題名から版を除いた。
  `assets/README.md` gets a 9-3 header; the version is removed from its title.

### ひな形 / Templates
- `templates/.github/workflows/version-check.yml` と `release.yml` を追加(mdEditor の実装をもとに、Release の題名をリポジトリ名から作り、CHANGELOG の見出しは v のある形・ない形の両方を読む)。12-1 (2)・12-3 も更新。
  Workflow templates added, based on mdEditor's; the Release title comes from the repository name, and both heading forms are read.

## v4.11 — 2026-10-11

mdEditor(5garashi/mdEditor)のユニバーサルデザイン対応と出荷前チェックからの提案(16項目)を反映。
Sixteen proposals from mdEditor's universal-design work and pre-release check applied.

### 第3条・第2条・第4条 4-2(マーク)/ Mark
- 3-7 (5):シンプル版は暗い地でも volt のままでよいとした。守ることは (a) マークだけのボタン・リンクは灰色抜き(非テキスト 3:1)、(b) 状態や意味を伝えない、(c) 昼の ink に置かない、の3つ(以前の「名称を近くに示す」は外した)。
  3-7 (5): the simple mark may stay volt on dark grounds; three rules remain (gray reversal for mark-only controls, no state or meaning, never on the day ink). The "name nearby" condition is removed.
- 3-7 補:用途別の対応表(ヘッダー・ロゴタイプ・アイコン・マークだけのボタン・モチーフ・ink 地・白黒)を新設。2-2 と 4-2 (2) を合わせて改めた。
  New 3-7 (cont.) usage table; 2-2 and 4-2 (2) aligned.

### 第4条 / Art. 4
- 4-2 (1):選んだ表示を次回の起動でも使う。デスクトップアプリではタイトルバーも合わせる。
  4-2 (1): the chosen mode is kept; desktop apps match the title bar.
- 4-3:`--document-selection`(昼 `#C7D0C1`/夜 `#494740`)、`--document-current-line`(`#F0F0F0`/`#202122`)、`--document-reading`(`#B92613`/`#F07B5F`)を追加。(5) 印刷とPDFは余白を含めて白、(6) 選んだ範囲・いまの行の上でも文字の比を保つ、を追記。7-1 補2 に6組を追加(夜の選んだ範囲の文字は 5.06:1 でAA、ほかはAAAまたは非テキスト 3:1 以上)。
  4-3: three tokens added; white PDF margins; 7-1 (cont. 2) gains six pairs.

### 第6条 / Art. 6
- 「図(ライブラリが描く図)」の行を追加。英語の行名「FIGURES」を「NUMBERS / ANSWERS」に改めた(数値の規定を図の規定と読み違えないため)。
  New "Diagrams (library-drawn)" row; the English label "FIGURES" is now "NUMBERS / ANSWERS" to avoid confusion with diagrams.
- 「ユニバーサル」の注記に、使う人が選んだ書体・文字の大きさ・行間を優先することを追記。
  The Universal note now gives precedence to the user's chosen typeface, size, and spacing.

### 第7条 / Art. 7
- 7-3:見出しを「操作の原則」に改め、(2) にショートカットの一覧・ヒントと `aria-keyshortcuts`・OSのキーとぶつけない・`Esc` は固定・変えたキーの保存を、(4)「使う人の選択を優先」を追加。
  7-3: renamed "Rules of interaction"; shortcut rules added to (2); new (4) "The user's choice comes first".
- 7-4:文章の読み上げの決まり(読んでいる段落を示す・`Esc` で止まる・言語に合った音声・音声がないときの案内・PCの音声だけを使う)を追加。
  7-4: read-aloud rules added.
- 7-5:動きは `transition: none` / `animation: none` で止め、`transition-duration: 0.01ms` は使わないと明記(9-4 の見本はもともと `none`)。
  7-5: stop motion with `none`; never shorten `transition-duration` (the 9-4 sample already used `none`).
- 7-6:エラーやお知らせは、何が起きたかと次にすることを書く。
  7-6: errors and notices say what happened and what to do next.
- 7-7:(f) コントラストテーマ、(g) 画面読み上げソフト、(h) 文字の大きさの設定200%、(i) 復元を追加。
  7-7: checks (f)–(i) added.
- 7-8「コントラストテーマ(強制カラー)」、7-9「作業を失わせない」を新設。
  New 7-8 "Contrast themes (forced colors)" and 7-9 "Never lose the user's work".

### 第9条・第12条・第13条 / Arts. 9, 12, 13
- 9-3:(4) JSON と改変せずに同梱する第三者のファイルは対象外、(5) Markdown は HTML コメントに書く。
  9-3: exemptions and Markdown headers.
- 9-4:新しいトークンと、`@media (forced-colors: active)` の例を追加。
  9-4: new tokens and a forced-colors example.
- 9-5:アクセシビリティの確認記録のひな形を追加。
  9-5: accessibility check record template.
- 12-1:`templates/` のひな形を MIT とした。12-6「製品の配布物」(LICENSE・THIRD-PARTY-NOTICES.md・PRIVACY.md)を新設。
  12-1: templates are MIT; new 12-6 "Product distributions".
- 第13条「プライバシー」を新設(テレメトリ・広告の通信をしない、PCの中で処理する、保存するデータと場所を公開する、PRIVACY.md)。`templates/PRIVACY.md`(日英)を追加。
  New Art. 13 "Privacy"; `templates/PRIVACY.md` (JA/EN) added.

### ページ・ツール / Page and tools
- 本書自体をコントラストテーマに対応(色見本・マーク・ロゴ・表の見本は元の色を保ち、番号札やバッジには枠を付ける)。
  This document now supports contrast themes.
- `tools/check_contrast.py`:文書面の新しい組を追加。
  `tools/check_contrast.py`: new document-surface pairs.
- 単一ファイル版のファイル名を `5garashi_identity_v4_11.html` に変更。
  Single-file edition renamed to `5garashi_identity_v4_11.html`.

## v4.10 — 2026-10-11

### 本文 / Content
- 第9条 9-3:ファイルヘッダーの項目名をファイルの言語に合わせるとした。日本語を含むファイルは日英併記(見本A)、説明やコメントを英語だけで書くファイル(英語版)は英語の項目名だけ(見本B:`File:`、`Description:`、`Author:`、`Created:`、`License:`)。作成者の欄はどちらも 8-6 の公式表記(日英併記)とする。
  Art. 9-3: file-header labels follow the file's language — bilingual for files containing Japanese (sample A), English only for files written only in English (sample B). The author field always uses the official paired name of 8-6.
- 9-3 の見本の「作成日 / Date」を「作成日 / Created」に統一(本書・各ファイル・mdEditor の実際の表記に合わせた)。第12条 12-1 の参照も「見本A・B」に更新。
  The 9-3 sample label "Date" is now "Created", matching actual files; Art. 12-1 now refers to samples A and B.
- 9-3 見本B(英語版)の作成者を英語表記「5garashi.com Design Office」とした。8-6 の「ファイルヘッダーでは常に併記形」にも、英語だけで書くファイルの例外を追記。
  Sample B (English edition) uses the English name "5garashi.com Design Office" as author; the matching exception is added to 8-6.
- 第4条 4-3:文書面の昼の区切り線 `--document-rule` を `#DFCF9A` から `#D0D0D0` に変更。文書面は無彩色の機能色とする方針(4-3)に合わせた。白地に対して 1.54:1 で、装飾専用のため基準の対象外(変更前は 1.55:1)。7-1 補2 と 9-4 も更新。
  Art. 4-3: the day document rule changes from `#DFCF9A` to neutral `#D0D0D0` (1.54:1 on white, decorative only), matching the neutral document surface; 7-1 (cont. 2) and 9-4 updated.
- 第6条:英語表示の欧文書体を追加。OSの標準UI書体(`"Segoe UI", -apple-system, BlinkMacSystemFont, "Noto Sans"`)の後に和文書体を続ける。`system-ui` は日本語版のOSで和文UI書体になることがあるため先頭に置かない。ロゴの「5」と等幅書体は変えない。本書の英語表示にも適用。
  Art. 6: Latin typeface for English display — the OS UI face followed by the Japanese stack; `system-ui` is not placed first because it can resolve to a Japanese face. Applied to this document's English view.

### ページ / Page
- 単一ファイル版のファイル名を `5garashi_identity_v4_10.html` に変更。
  Single-file edition renamed to `5garashi_identity_v4_10.html`.

## v4.9 — 2026-10-11

mdEditor(5garashi/mdEditor)のダークモード実装からの提案を反映。
Proposal from the mdEditor (5garashi/mdEditor) dark-mode implementation applied.

### 本文 / Content
- 第4条 4-2:夜の ink を `#EFE6C4` から `#C9C1A5` に変更(RGB値で84%、相対輝度で約68%)。暗い画面でボタンの文字・枠・欄の枠線がまぶしかったため。夜のすべての ink に適用し、本書自体の夜の表示も同じ値にした。
  Art. 4-2: night ink changed from `#EFE6C4` to `#C9C1A5` (84% in RGB, about 68% in relative luminance) because buttons, borders, and field outlines glared on dark screens. Applied to all night ink, including this document.
- 第4条:4-3「文書面(編集欄・プレビュー)の色」を新設。長文を読み書きする面には無彩色の機能色を使い、コード表示ブロックと同じくパレットの例外とする。`--document-background`(昼 `#FFFFFF`/夜 `#121314`)、`--document-foreground`(昼 `#1A1A1A`/夜 `#BFBFBF`)、`--document-rule`(昼 `#DFCF9A`/夜 `#2B2B2B`、装飾専用)。
  Art. 4: new 4-3 "Document surface": neutral functional colors for long-text surfaces, an exception to the palette like the code-block colors.
- `--document-rule` は装飾専用で文字の基準の対象外とし、見出しは下線なしでも大きさ・太さで見分けられることを条件とした。
  `--document-rule` is decorative only and exempt, on condition that headings remain identifiable by size and weight without it.
- 第7条 7-1 補:夜の ink の組を更新(ink × paper 9.09:1 AAA、ink × card 8.08:1 AAA、ink × head と head × ink 6.74:1 AA。20組中11組がAAA)。夜の volt × ink は 1.51:1 で、引き続き重ねない。
  Art. 7-1 (cont.): night ink pairs updated (20 pairs, 11 AAA); night volt on ink is 1.51:1 and stays prohibited.
- 第7条 7-1 補2:文書面のコントラスト対照表を新設(昼:本文 17.40:1、エラー文字 9.22:1、エラー左罫 6.27:1。夜:本文 10.12:1、エラー文字 9.50:1、エラー左罫 6.82:1)。
  Art. 7-1 (cont. 2): new contrast table for the document surface.
- 第9条 9-4:CSSトークンに `--document-*` の3つを追加し、夜の ink を更新。
  Art. 9-4: three `--document-*` tokens added; night ink updated.
- 第4条 4-3 (4):文書面の本文の太さを W4(400)とした(第6条の本文 W6 の例外)。見出しは W7 以上で、下線なしで見分けられること。第6条の本文の行にも参照を追記。
  Art. 4-3 (4): document-surface body text is W4 (400), an exception to Art. 6; headings W7 or heavier. Cross-reference added to Art. 6.
- 第4条 4-2 (1):利用者が表示の切り替えで夜を選んだときも夜の配色を使う。切り替えを設ける場合は、環境に従う設定を既定とし、選ばれている表示を文字で示す。
  Art. 4-2 (1): the night palette also applies when the user chooses it; a switch defaults to following the environment and shows the current choice in words.
- 第3条 3-7 (5):暗い地(夜の配色の地、OSが描く暗いタイトルバーなど)でも、シンプル版を volt のまま置いてよいとした。ロゴはコントラスト基準の対象外だが、比は 1.94〜2.61:1、P型の色覚のシミュレーションでは 1.39〜1.88:1 まで下がるため、(a) 名称を近くに示す、(b) マークだけでボタンやリンクにしない、(c) 状態や意味を伝えない、(d) 昼の ink の上に置かない、をすべて満たすことを条件とした。4-2 (2) にも参照を追記。
  Art. 3-7 (5): the simple mark may stay volt on dark grounds (night grounds, dark OS title bars) under four conditions — name shown nearby, never an icon-only control, never carries state or meaning, never on the day ink — because the ratio is 1.94–2.61:1 and 1.39–1.88:1 under protan simulation.
- 第9条 9-2:ファビコンとアプリアイコンは表示モードによらず volt のシンプル版とすることを明記。
  Art. 9-2: favicons and app icons stay the volt simple mark in every display mode.
- 第10条:volt と重ねてはいけない ink が昼の ink `#385723` であることを明記。
  Art. 10: clarified that the forbidden ink is the day ink `#385723`.

### ツール / Tools
- `tools/check_contrast.py`:夜の ink を更新し、文書面の組(文字・非テキスト・装飾)を追加。
  `tools/check_contrast.py`: night ink updated; document-surface pairs added (text, non-text, decorative).
- `tools/check_contrast.py`:暗い地での volt のマークについて、色覚の多様性のシミュレーション(Machado ほか 2009、P型・D型)による比を参考として出力するようにした。
  `tools/check_contrast.py`: prints protan/deutan-simulated ratios (Machado et al. 2009) for the volt mark on dark grounds.
- 単一ファイル版のファイル名を `5garashi_identity_v4_9.html` に変更。
  Single-file edition renamed to `5garashi_identity_v4_9.html`.

## v4.8 — 2026-10-11

ダークモードの配色を追加。
Dark-mode colors added.

### 本文 / Content
- 第4条:4-2「夜の配色(ダークモード)」を新設。ink(千歳緑)を深く沈めた地に paper(鳥の子色)の文字を置く11色(paper `#1A2212`、card `#222C1A`、head `#2B3A20`、ink `#EFE6C4`、steel `#D9B98C`、volt `#F07B5F`、volt-deep `#F7A58E`、line `#4C5C3B`、ok `#9FCC7E`、cream `#1A2212`、mark `#ADADA5`)。変数名は昼と同じで値だけを入れ替える。印刷は常に昼の配色。
  Art. 4: new 4-2 "Night palette (dark mode)" — eleven colors with paper-colored text on deeply sunk ink. Same variable names, different values. Print always uses the day palette.
- 第3条:3-7「ダークモード用の反転版(灰色抜き)」を新設。ダークモードでは、シンボルマークとロゴタイプを灰 `#ADADA5`(和名のめやす:銀鼠)で抜き、地を透明にした反転版を使う。paper やクリームイエローは暗い画面でまぶしいため、明るさを paper の約半分に抑えた。昼の volt は夜の地に対して 2.61:1 で、マークの色を明るく変えることは第10条で禁止しているため、マークも灰色で抜く。夜の volt はアクセントとフォーカス枠専用。第3条の見本・色見本・マーク見本・禁止例は昼の配色のまま表示する。2-2、3-1、第5条、第10条の例外にも同じ規定を追記。
  Art. 3: new 3-7 "Reversed version for dark mode (gray)". In dark mode the mark and logotype are reversed in gray `#ADADA5` on a transparent ground; paper and cream yellow glare on dark screens. Specimens stay in day colors. Exceptions added to 2-2, 3-1, Art. 5, and Art. 10.
- アセット:`5garashi_logotype_reversed.svg`、`5garashi_logotype_reversed_outlined.svg`、`5garashi_logotype_en_reversed.svg`、`5garashi_logotype_en_reversed_outlined.svg`、`5garashi_mark_simple_reversed_gray.svg` を追加(白黒版の色を置き換えて作成)。
  Assets: five gray reversed SVGs added, derived from the monochrome versions.
- 第7条 7-1:夜の配色のコントラスト対照表を追加(20組、すべてAA以上、13組がAAA。灰色抜きの3組を含む)。夜の配色でも volt と ink は重ねない(2.18:1)。7-7 の出荷前チェックに (e) ダークモードでの確認を追加。
  Art. 7-1: night contrast table added (20 pairs, all AA or better, 13 AAA, including three for the gray reversal); volt and ink never layered at night either (2.18:1). 7-7 adds (e) dark-mode check.
- 第9条 9-4:CSSトークンに夜の配色の `@media (prefers-color-scheme: dark)` ブロックと、マークの色 `--mark` を追加。
  Art. 9-4: CSS tokens gain the night `@media (prefers-color-scheme: dark)` block and the mark color `--mark`.

### ページ / Page
- 本書自体をダークモードに対応(`color-scheme`、ダーク用 `theme-color`、`.specimen` による見本図の昼配色の保持)。昼の表示は v4.7 から変わらない。
  This document now supports dark mode (`color-scheme`, dark `theme-color`, `.specimen` keeps figures in day colors). The day appearance is unchanged from v4.7.
- `tools/check_contrast.py` に夜の配色と、その許可組・禁止組を追加。
  `tools/check_contrast.py` now covers the night palette, its approved pairs, and forbidden pair.
- 単一ファイル版のファイル名を `5garashi_identity_v4_8.html` に変更。
  Single-file edition renamed to `5garashi_identity_v4_8.html`.

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
**最終更新 / Last updated**: 2026-10-12 JST
