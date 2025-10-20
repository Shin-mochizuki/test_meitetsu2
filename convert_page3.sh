#!/bin/bash

INPUT_DIR="/Users/s.mochizuki/Documents/20251019_名鉄GitHub調整/workspace/page3_個人Excel"
OUTPUT_DIR="/Users/s.mochizuki/Documents/20251019_名鉄GitHub調整/workspace/page3_PDFver"

# LibreOfficeの実行ファイルのパスを指定
LIBREOFFICE_PATH="/Applications/LibreOffice.app/Contents/MacOS/soffice"

for FILE in "$INPUT_DIR"/*.xlsx; do
    "$LIBREOFFICE_PATH" --headless --convert-to pdf --outdir "$OUTPUT_DIR" "$FILE"
    echo "Converted $FILE to PDF."
done
