#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jupyter MCP Server - Jupyter NotebookをMCPサーバーとして公開
"""

__version__ = "0.1.0"

from .jupyter_mcp_server import JupyterMCP

def main():
    """コマンドラインエントリポイント"""
    jupyter_mcp = JupyterMCP()
    jupyter_mcp.run()

if __name__ == "__main__":
    main()
