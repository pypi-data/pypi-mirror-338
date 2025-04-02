#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
テスト用のサンプルノートブックを作成するためのスクリプト
"""

import os
import nbformat
from pathlib import Path


def create_sample_notebook(output_path=None):
    """
    テスト用のサンプルノートブックを作成する
    
    Args:
        output_path: 出力先パス (指定がなければ notebooks/test_sample.ipynb に作成)
    
    Returns:
        作成したノートブックのパス
    """
    if output_path is None:
        # テストディレクトリからの相対パス
        tests_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        project_root = os.path.dirname(tests_dir)
        output_path = os.path.join(project_root, "notebooks", "test_sample.ipynb")
    
    # 新しいノートブックを作成
    notebook = nbformat.v4.new_notebook()
    
    # マークダウンセルを追加
    markdown_cell1 = nbformat.v4.new_markdown_cell("""
# テスト用サンプルノートブック

このノートブックは、テスト用に自動生成されたものです。
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
    'A': np.random.rand(5),
    'B': np.random.rand(5),
    'C': np.random.rand(5)
}

df = pd.DataFrame(data)
df
""")
    
    code_cell3 = nbformat.v4.new_code_cell("""
# 簡単な計算
2 + 2
""")
    
    # セルをノートブックに追加
    notebook.cells.extend([
        markdown_cell1, 
        code_cell1, 
        code_cell2, 
        code_cell3
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
            "version": "3.13.2"
        }
    }
    
    # 保存先ディレクトリを作成
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # ノートブックを保存
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    
    print(f"テスト用サンプルノートブックを作成しました: {output_path}")
    return output_path


if __name__ == "__main__":
    # スクリプトとして実行された場合はサンプルノートブックを作成
    create_sample_notebook() 
