#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcp.server.fastmcp import FastMCP
import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager
import json
import os
from pathlib import Path
import tempfile

class JupyterMCP:
    def __init__(self, name="JupyterMCP"):
        self.mcp = FastMCP(name)
        self.setup_resources()
        self.setup_tools()
        
        # カレントノートブックとクライアント
        self.current_notebook = None
        self.current_notebook_path = None
        self.notebook_client = None
        self.kernel_id = None
        
        # カーネル仕様マネージャー
        self.kernel_manager = KernelSpecManager()
    
    def setup_resources(self):
        """リソースの設定"""
        
        @self.mcp.resource("notebook://{path}")
        def get_notebook(path: str) -> str:
            """ノートブックの内容を取得するリソース"""
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)
                    return json.dumps(notebook, indent=2)
            except Exception as e:
                return f"Error loading notebook: {str(e)}"
        
        @self.mcp.resource("cell://{path}/{cell_index}")
        def get_cell(path: str, cell_index: int) -> str:
            """特定のセルの内容を取得するリソース"""
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                cell = notebook.cells[cell_index]
                return json.dumps(cell, indent=2)
            except Exception as e:
                return f"Error loading cell: {str(e)}"
        
        @self.mcp.resource("cell_output://{path}/{cell_index}")
        def get_cell_output(path: str, cell_index: int) -> str:
            """特定のセルの出力を取得するリソース"""
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                cell = notebook.cells[cell_index]
                if 'outputs' not in cell:
                    return "No outputs available for this cell"
                
                return json.dumps(cell.outputs, indent=2)
            except Exception as e:
                return f"Error loading cell output: {str(e)}"
        
        @self.mcp.resource("kernels://list")
        def list_kernels() -> str:
            """利用可能なカーネルの一覧を取得するリソース"""
            try:
                kernel_specs = self.kernel_manager.get_all_specs()
                return json.dumps(kernel_specs, indent=2)
            except Exception as e:
                return f"Error listing kernels: {str(e)}"
    
    def setup_tools(self):
        """ツールの設定"""
        
        @self.mcp.tool()
        def open_notebook(path: str) -> str:
            """ノートブックを開くツール"""
            try:
                abs_path = os.path.abspath(path)
                
                # ノートブックが存在しない場合は新規作成
                if not os.path.exists(abs_path):
                    notebook = nbformat.v4.new_notebook()
                    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                    with open(abs_path, 'w', encoding='utf-8') as f:
                        nbformat.write(notebook, f)
                
                # 既存のノートブックを読み込む
                with open(abs_path, 'r', encoding='utf-8') as f:
                    self.current_notebook = nbformat.read(f, as_version=4)
                
                self.current_notebook_path = abs_path
                
                # クライアントを初期化（まだ実行はしない）
                self.notebook_client = NotebookClient(
                    self.current_notebook,
                    timeout=600,
                    kernel_name="python3"
                )
                
                return f"Successfully opened notebook: {abs_path}"
            except Exception as e:
                return f"Error opening notebook: {str(e)}"
        
        @self.mcp.tool()
        def save_notebook() -> str:
            """現在のノートブックを保存するツール"""
            try:
                if self.current_notebook is None or self.current_notebook_path is None:
                    return "No notebook is currently open"
                
                with open(self.current_notebook_path, 'w', encoding='utf-8') as f:
                    nbformat.write(self.current_notebook, f)
                
                return f"Successfully saved notebook to {self.current_notebook_path}"
            except Exception as e:
                return f"Error saving notebook: {str(e)}"
        
        @self.mcp.tool()
        def get_cell_count() -> str:
            """現在のノートブックのセル数を取得するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                return str(len(self.current_notebook.cells))
            except Exception as e:
                return f"Error getting cell count: {str(e)}"
        
        @self.mcp.tool()
        def add_code_cell(source: str, position: int = -1) -> str:
            """コードセルを追加するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                new_cell = nbformat.v4.new_code_cell(source=source)
                
                if position < 0 or position >= len(self.current_notebook.cells):
                    # デフォルトは末尾に追加
                    self.current_notebook.cells.append(new_cell)
                    position = len(self.current_notebook.cells) - 1
                else:
                    # 指定位置に挿入
                    self.current_notebook.cells.insert(position, new_cell)
                
                return f"Added code cell at position {position}"
            except Exception as e:
                return f"Error adding code cell: {str(e)}"
        
        @self.mcp.tool()
        def add_markdown_cell(source: str, position: int = -1) -> str:
            """マークダウンセルを追加するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                new_cell = nbformat.v4.new_markdown_cell(source=source)
                
                if position < 0 or position >= len(self.current_notebook.cells):
                    # デフォルトは末尾に追加
                    self.current_notebook.cells.append(new_cell)
                    position = len(self.current_notebook.cells) - 1
                else:
                    # 指定位置に挿入
                    self.current_notebook.cells.insert(position, new_cell)
                
                return f"Added markdown cell at position {position}"
            except Exception as e:
                return f"Error adding markdown cell: {str(e)}"
        
        @self.mcp.tool()
        def edit_cell(cell_index: int, source: str) -> str:
            """セルを編集するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(self.current_notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                # セルのソースコードを更新
                self.current_notebook.cells[cell_index].source = source
                
                return f"Edited cell at index {cell_index}"
            except Exception as e:
                return f"Error editing cell: {str(e)}"
        
        @self.mcp.tool()
        def delete_cell(cell_index: int) -> str:
            """セルを削除するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(self.current_notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                # セルを削除
                del self.current_notebook.cells[cell_index]
                
                return f"Deleted cell at index {cell_index}"
            except Exception as e:
                return f"Error deleting cell: {str(e)}"
        
        @self.mcp.tool()
        def execute_cell(cell_index: int) -> str:
            """特定のセルを実行するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                if self.notebook_client is None:
                    return "Notebook client is not initialized"
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(self.current_notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                # 一時ファイルにノートブックを保存
                with tempfile.NamedTemporaryFile(suffix='.ipynb', delete=False) as tmp:
                    tmp_path = tmp.name
                    nbformat.write(self.current_notebook, tmp)
                
                try:
                    # 実行用のクライアントを作成
                    client = NotebookClient(
                        self.current_notebook,
                        timeout=600,
                        kernel_name="python3"
                    )
                    
                    # 指定されたセルを実行
                    client.execute_cell(self.current_notebook.cells[cell_index], cell_index)
                    
                    # 実行結果を取得
                    cell = self.current_notebook.cells[cell_index]
                    if hasattr(cell, 'outputs') and cell.outputs:
                        # 出力がある場合は要約して返す
                        output_summary = []
                        for output in cell.outputs:
                            if output.output_type == 'stream':
                                output_summary.append(f"Stream output: {output.text[:200]}...")
                            elif output.output_type == 'display_data':
                                output_summary.append(f"Display data: {list(output.data.keys())}")
                            elif output.output_type == 'execute_result':
                                output_summary.append(f"Execute result: {list(output.data.keys())}")
                            else:
                                output_summary.append(f"Other output: {output.output_type}")
                        
                        return f"Cell executed successfully. Outputs: {'; '.join(output_summary)}"
                    else:
                        return "Cell executed successfully. No outputs."
                    
                finally:
                    # 一時ファイルを削除
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path)
                
            except Exception as e:
                return f"Error executing cell: {str(e)}"
        
        @self.mcp.tool()
        def execute_notebook() -> str:
            """ノートブック全体を実行するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                # 一時ファイルにノートブックを保存
                with tempfile.NamedTemporaryFile(suffix='.ipynb', delete=False) as tmp:
                    tmp_path = tmp.name
                    nbformat.write(self.current_notebook, tmp)
                
                try:
                    # 実行用のクライアントを作成
                    client = NotebookClient(
                        self.current_notebook,
                        timeout=600,
                        kernel_name="python3"
                    )
                    
                    # ノートブック全体を実行
                    client.execute()
                    
                    return "Notebook executed successfully"
                    
                finally:
                    # 一時ファイルを削除
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path)
                
            except Exception as e:
                return f"Error executing notebook: {str(e)}"
        
        @self.mcp.tool()
        def get_cell_source(cell_index: int) -> str:
            """セルのソースコードを取得するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(self.current_notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                return self.current_notebook.cells[cell_index].source
            except Exception as e:
                return f"Error getting cell source: {str(e)}"
        
        @self.mcp.tool()
        def get_cell_outputs(cell_index: int) -> str:
            """セルの出力を取得するツール"""
            try:
                if self.current_notebook is None:
                    return "No notebook is currently open"
                
                cell_index = int(cell_index)
                if cell_index < 0 or cell_index >= len(self.current_notebook.cells):
                    return f"Invalid cell index: {cell_index}"
                
                cell = self.current_notebook.cells[cell_index]
                
                if not hasattr(cell, 'outputs') or not cell.outputs:
                    return "No outputs available for this cell"
                
                # 出力を文字列形式で返す
                outputs_str = []
                for i, output in enumerate(cell.outputs):
                    outputs_str.append(f"Output {i}:")
                    if output.output_type == 'stream':
                        outputs_str.append(f"  Stream: {output.text}")
                    elif output.output_type == 'display_data':
                        outputs_str.append(f"  Data: {list(output.data.keys())}")
                        if 'text/plain' in output.data:
                            outputs_str.append(f"  Text: {output.data['text/plain']}")
                    elif output.output_type == 'execute_result':
                        outputs_str.append(f"  Data: {list(output.data.keys())}")
                        if 'text/plain' in output.data:
                            outputs_str.append(f"  Text: {output.data['text/plain']}")
                    elif output.output_type == 'error':
                        outputs_str.append(f"  Error: {output.ename}: {output.evalue}")
                        if hasattr(output, 'traceback'):
                            outputs_str.append("  Traceback:")
                            for line in output.traceback:
                                outputs_str.append(f"    {line}")
                
                return "\n".join(outputs_str)
            except Exception as e:
                return f"Error getting cell outputs: {str(e)}"
    
    def run(self, host="127.0.0.1", port=8000):
        """MCPサーバーを実行する"""
        self.mcp.run(host=host, port=port)


if __name__ == "__main__":
    jupyter_mcp = JupyterMCP()
    jupyter_mcp.run() 
