# Jupyter MCP Server - ソースコード

このディレクトリにはJupyter MCP Serverのソースコードが含まれています。

## ファイル構成

- `jupyter_mcp_server.py` - メインのサーバー実装
- `create_sample_notebook.py` - サンプルノートブックの作成ユーティリティ
- `__init__.py` - パッケージ初期化ファイル

## 使用方法

モジュールとして使用する場合：

```python
from jupyter_mcp_server import JupyterMCP

jupyter_mcp = JupyterMCP()
jupyter_mcp.run()
```

コマンドラインから実行する場合：

```bash
python -m jupyter_mcp_server
# または
jupyter-mcp-server
```

## ファイル詳細

### jupyter_mcp_server.py

Jupyter NotebookをMCPサーバーとして公開するためのメインクラスが含まれています。
このモジュールは以下の機能を提供します：

- MCPリソースとツールの定義
- ノートブック操作（開く、保存、セル追加など）
- セル実行と結果取得

### create_sample_notebook.py

テスト用やデモ用のサンプルノートブックを作成するためのユーティリティスクリプトです。 
