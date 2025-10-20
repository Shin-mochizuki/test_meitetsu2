# 名鉄FY24レポート作成コード

本リポジトリは、FY24より導入した**カスタマイズレポート返却**の作成工程と、準備すべき資料一覧を整理したものです。  
ノートブック・スクリプト・テンプレートを使って、P1〜P4 の最終PDFを作成します。

---

## 目的
FY24より受検結果をカスタマイズレポートで返却している。  
本リポジトリは、その**作成工程**と**準備資料**を明確化するための資料である。

---

## 前提 / 動作環境

- macOS（Linux可）
- Python 3.9+ 推奨
- LibreOffice（Excel→PDF 変換で使用）  
  → [公式サイト](https://www.libreoffice.org/download/download-libreoffice/) からインストール

**Python ライブラリ（例）**
```txt
numpy
pandas
scipy
matplotlib
seaborn
pymupdf           # import fitz
Pillow
PyPDF2
reportlab
openpyxl
tqdm
jupyter
```

> プロジェクトで `requirements.txt` を用意する場合は上記をベースに調整してください。

---

## ディレクトリ構成（抜粋）

```
/20251019_名鉄GitHub調整
├── FY24_main.ipynb                 # メインノートブック
├── First_cell_code.txt             # ノート冒頭セルの参照コード
├── convert_page2.sh / convert_page3.sh
├── add_gitkeep.sh                  # 空フォルダ保持用（任意）
├── lib/                            # コード（データ処理・可視化・設定・SQL）
│   ├── data/                       # データ定義・DB等
│   ├── op/                         # プロット・統計等のオペレーション
│   ├── graphs.py / setting.py / sql.py
├── import/                         # 入力データ配置（.gitignore 対象）
├── workspace/                      # 作業用Excel/PDF配置（.gitignore 対象）
├── export/ / deliverables/         # 出力/納品物（.gitignore 対象）
├── materials/ / models/            # 参考資料/モデル（.gitignore 対象）
└── .gitignore
```

> 大型/機微データは `.gitignore` で除外。空フォルダ維持は `.gitkeep` を使用。

---

## 初期設定

### 1. 実データの追加

**`import/` に追加するデータ**
- [99_dat_Bench_max100.csv](https://drive.google.com/file/d/1ZB_Ali3mfgTFd9J2yKtEwsSO4fYJgARB/view?usp=drive_link)
- [F1040-03_2024-11-07 00:00:00_2024年度360度評価_補正済みスコア.csv](https://drive.google.com/file/d/1LtitPde70vjL4Vhysn4Gvtgb1Pr67coU/view?usp=drive_link)
- [所属追加_F1040名古屋鉄道株式会社様_ユーザ゙ーリスト.xlsx](https://docs.google.com/spreadsheets/d/1LvRDR2JUJ_kOK72_pvvMtPG2ReH_g5y8/edit?usp=drive_link&ouid=101274500552420687286&rtpof=true&sd=true)

**`workspace/` に追加するデータ**
- [1217_P1【名鉄】カスタマイズレポート_Excel調整_最終.pdf](https://drive.google.com/file/d/1esgN4d9VJhCpLYVehRwtKMab6yBTTf_I/view?usp=drive_link)
- [1217_P4【名鉄】カスタマイズレポート_Excel調整_最終.pdf](https://drive.google.com/file/d/1euEqzi6kRwyl0zT5ymaD1uBBffkgnVQH/view?usp=drive_link)
- [【名鉄】カスタマイズレポート_Excel調整_最終_望月編集_p2.xlsx](https://docs.google.com/spreadsheets/d/1MxY5APoAlwvvKuWhqaRgJRfKEAM9QUjb/edit?usp=drive_link&ouid=101274500552420687286&rtpof=true&sd=true)
- [【名鉄】カスタマイズレポート_Excel調整_最終_望月編集_p3.xlsx](https://docs.google.com/spreadsheets/d/1MvqV-o3FXa9YVMPYKvbtM6zf3ab9EfZf/edit?usp=drive_link&ouid=101274500552420687286&rtpof=true&sd=true)

### 2. LibreOffice の設定
Excel ⇨ PDF 変換に使用します。  
上記公式サイトよりインストールのうえ、後述のスクリプトで `soffice` のパスを指定してください。

---

## 作業工程

1. **案件共有書作成**
   - 【HCM】前回からの変更点を確認し、資料作成
   - 【DC】上記資料をもとにロジック仕様書の作成(更新)

2. **テンプレート作成**
   - 【HCM】P1, P4 の固定表示ページの文言調整（PDF保存）
   - 【DC】P2, P3 の Excel テンプレート更新

3. **【DC】作成作業**
   - コード修正  
     1) 仕様書に基づく仕様変更  
     2) データの入れ替え  
     3) プロット作成
   - **P2**  
     1) Excel へのデータ貼り付け保存  
     2) Excel ⇨ PDF 変換
   - **P3**  
     1) 「強み/弱み」部分の作成（Python→PDF）  
     2) PDF の画像化（jpeg 変換）  
     3) Excel テンプレに貼り付け
   - **P2 & P3 のPDF化**  
     1) Excel ⇨ PDF 変換
   - **concat**  
     1) P1〜P4 の結合  
     2) 仕様書に基づく命名規則で保存

4. **GitHub レビュー**

5. **成果物チェック**

---

## 準備すべき資料

- **デフォルト**
  - 顧客要望書
  - 案件共有書
  - ロジック仕様書
- **PDF**
  - P1 固定表示内容
  - P4 固定表示内容
- **Excel → PDF 変換スクリプト**
  - 環境依存だが LibreOffice による変換を採用

---

## LibreOffice による Excel→PDF 変換スクリプト

### 1) 前提
- macOS / Linux
- LibreOffice インストール済み（`soffice` コマンドがあること）

### 2) スクリプト概要
`convert_excel_to_pdf.sh`  
指定ディレクトリ内の `.xlsx` を一括で PDF に変換（ヘッドレス）。

```bash
#!/bin/bash

INPUT_DIR="/path/to/input_dir"
OUTPUT_DIR="/path/to/output_dir"
LIBREOFFICE_PATH="/Applications/LibreOffice.app/Contents/MacOS/soffice"  # macOS の例

mkdir -p "$OUTPUT_DIR"

for FILE in "$INPUT_DIR"/*.xlsx; do
  [ -e "$FILE" ] || continue
  "$LIBREOFFICE_PATH" --headless --norestore --invisible     --convert-to pdf --outdir "$OUTPUT_DIR" "$FILE"
  echo "Converted $FILE -> $OUTPUT_DIR/$(basename "${FILE%.xlsx}.pdf")"
done
```

### 3) 使い方
1. 任意の場所に保存（例：`workspace/convert_excel_to_pdf.sh`）  
2. 実行権限付与  
   ```bash
   chmod +x workspace/convert_excel_to_pdf.sh
   ```
3. 変数 `INPUT_DIR` / `OUTPUT_DIR` / `LIBREOFFICE_PATH` を環境に合わせて修正  
4. 実行  
   ```bash
   ./workspace/convert_excel_to_pdf.sh
   ```

### 4) 出力
`$OUTPUT_DIR` に `.pdf` が生成（拡張子のみ `.pdf` に置換）。

---

## ノートブック実行（FY24_main.ipynb）

1. 依存関係をインストール（必要に応じて仮想環境を使用）
   ```bash
   pip install -r requirements.txt
   ```
2. `import/`・`workspace/` に初期データを配置
3. `FY24_main.ipynb` を開き、**冒頭セル**（`First_cell_code.txt` 参照）から順に実行
4. `export/` または `deliverables/` に成果物が出力されることを確認

---

## Git 運用メモ

- **`.gitignore`** でデータ/成果物/作業物を除外  
- 空ディレクトリを維持したい場合は **`.gitkeep`** を使用  
  ```bash
  chmod +x add_gitkeep.sh
  ./add_gitkeep.sh
  ```
- 大型バイナリ（PDF/Excel等）を履歴管理する場合は **Git LFS** を検討

---

## セキュリティ / 機密情報

- APIキー/パスワード等は **コミットしない**（`.env` に置き `.gitignore` で除外）  
- `lib/setting.py` に秘匿情報がある場合は環境変数化して `os.getenv` で参照

---
