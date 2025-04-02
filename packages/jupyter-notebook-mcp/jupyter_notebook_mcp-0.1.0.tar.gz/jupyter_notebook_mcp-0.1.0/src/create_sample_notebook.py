#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nbformat
import os
from pathlib import Path

def create_sample_notebook():
    # 新しいノートブックを作成
    notebook = nbformat.v4.new_notebook()
    
    # マークダウンセルを追加
    markdown_cell1 = nbformat.v4.new_markdown_cell("""
# Jupyter MCP サンプルノートブック

このノートブックは、Jupyter MCPサーバーの動作確認用のサンプルです。
""")
    
    # コードセルを追加
    code_cell1 = nbformat.v4.new_code_cell("""
# 基本的なライブラリをインポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# グラフをノートブック内に表示
%matplotlib inline
""")
    
    code_cell2 = nbformat.v4.new_code_cell("""
# サンプルデータを作成
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
}

df = pd.DataFrame(data)
df
""")
    
    code_cell3 = nbformat.v4.new_code_cell("""
# データをプロット
plt.figure(figsize=(10, 6))
for column in df.columns:
    plt.plot(df.index, df[column], label=column)
plt.legend()
plt.title('サンプルデータ')
plt.xlabel('インデックス')
plt.ylabel('値')
plt.grid(True)
plt.show()
""")
    
    markdown_cell2 = nbformat.v4.new_markdown_cell("""
## データの集計

基本的な統計情報を確認します。
""")
    
    code_cell4 = nbformat.v4.new_code_cell("""
# 統計情報
df.describe()
""")
    
    # セルをノートブックに追加
    notebook.cells.extend([
        markdown_cell1, 
        code_cell1, 
        code_cell2, 
        code_cell3, 
        markdown_cell2, 
        code_cell4
    ])
    
    # ノートブックのメタデータを設定
    notebook.metadata = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.12.2"
        }
    }
    
    # 保存先ディレクトリを作成
    os.makedirs(os.path.dirname("notebooks/sample.ipynb"), exist_ok=True)
    
    # ノートブックを保存
    with open("notebooks/sample.ipynb", "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    
    print(f"サンプルノートブックを作成しました: notebooks/sample.ipynb")

if __name__ == "__main__":
    create_sample_notebook() 
