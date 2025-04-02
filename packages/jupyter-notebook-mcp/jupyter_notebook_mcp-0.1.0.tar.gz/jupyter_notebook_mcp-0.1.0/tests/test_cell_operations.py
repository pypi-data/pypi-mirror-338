"""
セル操作に関するテスト
"""

import os
import pytest
import asyncio

from tests.conftest import extract_text_content


@pytest.mark.asyncio
async def test_add_code_cell(jupyter_mcp, temp_notebook):
    """コードセルを追加するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": temp_notebook})
    
    # 最初のセル数を取得
    cell_count_result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    initial_cell_count = int(extract_text_content(cell_count_result))
    
    # コードセルを追加
    code = "print('Test code cell')"
    result = await jupyter_mcp.mcp.call_tool("add_code_cell", {"source": code})
    result_text = extract_text_content(result)
    
    # 検証
    assert "Added code cell" in result_text
    
    # セル数が増えたことを確認
    cell_count_result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    new_cell_count = int(extract_text_content(cell_count_result))
    assert new_cell_count == initial_cell_count + 1


@pytest.mark.asyncio
async def test_add_markdown_cell(jupyter_mcp, temp_notebook):
    """マークダウンセルを追加するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": temp_notebook})
    
    # 最初のセル数を取得
    cell_count_result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    initial_cell_count = int(extract_text_content(cell_count_result))
    
    # マークダウンセルを追加
    markdown = "## Test Markdown\nThis is a test."
    result = await jupyter_mcp.mcp.call_tool("add_markdown_cell", {"source": markdown})
    result_text = extract_text_content(result)
    
    # 検証
    assert "Added markdown cell" in result_text
    
    # セル数が増えたことを確認
    cell_count_result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    new_cell_count = int(extract_text_content(cell_count_result))
    assert new_cell_count == initial_cell_count + 1


@pytest.mark.asyncio
async def test_edit_cell(jupyter_mcp, temp_notebook):
    """セルを編集するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": temp_notebook})
    
    # 編集するセルのインデックス（2番目のセル = インデックス1）
    cell_index = 1
    
    # 新しいソースコード
    new_code = "print('Edited cell')"
    
    # セルを編集
    result = await jupyter_mcp.mcp.call_tool("edit_cell", {"cell_index": cell_index, "source": new_code})
    result_text = extract_text_content(result)
    
    # 検証
    assert "Edited cell at index" in result_text
    
    # 編集されたセルの内容を確認
    source_result = await jupyter_mcp.mcp.call_tool("get_cell_source", {"cell_index": cell_index})
    source = extract_text_content(source_result)
    assert source == new_code


@pytest.mark.asyncio
async def test_delete_cell(jupyter_mcp, temp_notebook):
    """セルを削除するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": temp_notebook})
    
    # 最初のセル数を取得
    cell_count_result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    initial_cell_count = int(extract_text_content(cell_count_result))
    
    # 削除するセルのインデックス（最後のセル）
    cell_index = initial_cell_count - 1
    
    # セルを削除
    result = await jupyter_mcp.mcp.call_tool("delete_cell", {"cell_index": cell_index})
    result_text = extract_text_content(result)
    
    # 検証
    assert "Deleted cell at index" in result_text
    
    # セル数が減ったことを確認
    cell_count_result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    new_cell_count = int(extract_text_content(cell_count_result))
    assert new_cell_count == initial_cell_count - 1


@pytest.mark.asyncio
async def test_get_cell_source(jupyter_mcp, sample_notebook_path):
    """セルのソースコードを取得するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": sample_notebook_path})
    
    # セルのソースコードを取得
    cell_index = 0  # 最初のセル
    result = await jupyter_mcp.mcp.call_tool("get_cell_source", {"cell_index": cell_index})
    source = extract_text_content(result)
    
    # 検証
    assert isinstance(source, str)
    assert len(source) > 0 
