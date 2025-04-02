"""
Jupyter MCPサーバーのテスト用共通フィクスチャ
"""

import os
import sys
import pytest
import tempfile
import nbformat
from pathlib import Path

# プロジェクトのルートパスをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jupyter_mcp_server import JupyterMCP


@pytest.fixture
def jupyter_mcp():
    """JupyterMCPインスタンスを提供するフィクスチャ"""
    return JupyterMCP()


@pytest.fixture
def sample_notebook_path():
    """サンプルノートブックへのパスを提供するフィクスチャ"""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                        "notebooks", "sample.ipynb")


@pytest.fixture
def temp_notebook():
    """一時的なノートブックファイルを作成して提供するフィクスチャ"""
    # 新しいノートブックを作成
    notebook = nbformat.v4.new_notebook()
    
    # マークダウンセルを追加
    markdown_cell = nbformat.v4.new_markdown_cell("# テスト用ノートブック")
    
    # コードセルを追加
    code_cell = nbformat.v4.new_code_cell("print('Hello, World!')")
    
    # セルをノートブックに追加
    notebook.cells.extend([markdown_cell, code_cell])
    
    # mkstempを使用して一時ファイルを作成
    fd, tmp_path = tempfile.mkstemp(suffix='.ipynb')
    os.close(fd)
    
    # ファイルに書き込む
    with open(tmp_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)
    
    yield tmp_path
    
    # テスト後にファイルを削除
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)


def extract_text_content(result):
    """MCPのテキストコンテンツリストから実際のテキスト値を取り出す"""
    if isinstance(result, list) and len(result) > 0:
        if hasattr(result[0], 'text'):
            return result[0].text
    return str(result) 
