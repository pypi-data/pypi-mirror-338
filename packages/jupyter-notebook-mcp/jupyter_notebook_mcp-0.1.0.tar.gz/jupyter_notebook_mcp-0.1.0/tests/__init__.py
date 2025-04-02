"""
Jupyter MCPサーバーのテストスイート
""" 

import os

# GitHub Issue #398の警告を抑制するために環境変数を設定
# https://github.com/jupyter/jupyter_core/issues/398
os.environ["JUPYTER_PLATFORM_DIRS"] = "1" 
