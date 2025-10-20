#!/bin/bash
# =====================================
# .gitkeep 追加スクリプト
# =====================================

# 対象フォルダ一覧
dirs=(
  "deliverables"
  "export"
  "import"
  "workspace"
  "materials"
  "models"
)

# 実行ディレクトリをスクリプトの場所に変更
cd "$(dirname "$0")" || exit 1

# 各フォルダを確認・作成し .gitkeep を配置
for d in "${dirs[@]}"; do
  if [ ! -d "$d" ]; then
    echo "📁 $d を作成します..."
    mkdir -p "$d"
  fi
  if [ ! -f "$d/.gitkeep" ]; then
    echo "📝 $d/.gitkeep を追加しました"
    touch "$d/.gitkeep"
  else
    echo "✅ $d/.gitkeep はすでに存在します"
  fi
done

echo "完了しました！"
