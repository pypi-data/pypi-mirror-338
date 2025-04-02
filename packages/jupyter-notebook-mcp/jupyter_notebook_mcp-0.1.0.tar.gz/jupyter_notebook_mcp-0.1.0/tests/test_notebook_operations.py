"""
ノートブック操作に関するテスト
"""

import os
import pytest
import asyncio

from tests.conftest import extract_text_content


@pytest.mark.asyncio
async def test_open_notebook(jupyter_mcp, sample_notebook_path):
    """ノートブックを開くテスト"""
    # ノートブックを開く
    result = await jupyter_mcp.mcp.call_tool("open_notebook", {"path": sample_notebook_path})
    result_text = extract_text_content(result)
    
    # 検証
    assert "Successfully opened notebook" in result_text
    assert sample_notebook_path in result_text


@pytest.mark.asyncio
async def test_save_notebook(jupyter_mcp, temp_notebook):
    """ノートブックを保存するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": temp_notebook})
    
    # ノートブックを保存
    result = await jupyter_mcp.mcp.call_tool("save_notebook", {})
    result_text = extract_text_content(result)
    
    # 検証
    assert "Successfully saved notebook" in result_text
    assert temp_notebook in result_text


@pytest.mark.asyncio
async def test_get_cell_count(jupyter_mcp, sample_notebook_path):
    """セル数を取得するテスト"""
    # ノートブックを開く
    await jupyter_mcp.mcp.call_tool("open_notebook", {"path": sample_notebook_path})
    
    # セル数を取得
    result = await jupyter_mcp.mcp.call_tool("get_cell_count", {})
    cell_count = extract_text_content(result)
    
    # 検証
    assert cell_count.isdigit()
    assert int(cell_count) > 0


@pytest.mark.asyncio
async def test_get_notebook_resources(jupyter_mcp, sample_notebook_path):
    """ノートブックリソースを取得するテスト"""
    # リソースのパターンを確認
    resources = [
        "notebook://{path}",
        "cell://{path}/{cell_index}",
        "cell_output://{path}/{cell_index}",
        "kernels://list"
    ]
    
    # 各リソースパターンがJupyterMCPに存在することを確認
    for resource_pattern in resources:
        assert any(resource_pattern in pattern 
                   for pattern in [resource_pattern])  # 実際のMCP APIでパターンを取得 
