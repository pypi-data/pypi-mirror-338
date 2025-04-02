# リリースプロセス

このドキュメントでは、Jupyter Notebook MCPパッケージをリリースする手順について説明します。

## 前提条件

- PyPIアカウント
- GitHub CLIまたはウェブインターフェース
- 必要な権限（リポジトリ管理者またはオーナー）

## リリース準備

1. **コードの準備**
   - すべてのテストが通過していることを確認
   ```bash
   python -m pytest
   ```
   - ドキュメントが最新であることを確認
   - `pyproject.toml`のバージョン番号が適切に更新されていることを確認

2. **変更履歴の更新**
   - `CHANGELOG.md`を更新（まだない場合は作成）して、新しいバージョンの変更点を記録
   ```markdown
   ## [0.1.0] - 2025-MM-DD
   ### 追加
   - 新機能A
   - 新機能B
   
   ### 変更
   - 既存機能Cの改善
   
   ### 修正
   - バグ修正D
   ```

## リリースプロセス

### 手動リリース

1. **パッケージのビルド**
   ```bash
   python -m build
   ```

2. **Test PyPIへの公開**
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. **テスト公開のインストールテスト**
   ```bash
   pip install --index-url https://test.pypi.org/simple/ jupyter-notebook-mcp
   ```

4. **本番PyPIへの公開**
   ```bash
   python -m twine upload dist/*
   ```

### GitHub Actionsによる自動リリース

1. **GitHubリリースの作成**
   - GitHubのリポジトリページでReleasesタブに移動
   - 「Draft a new release」をクリック
   - タグを作成（例：v0.1.0）
   - リリースタイトルとリリースノートを入力
   - 「Publish release」をクリック

2. **ワークフローの監視**
   - GitHub Actionsタブでワークフローの実行を確認
   - 公開が成功したことを確認

3. **インストールテスト**
   ```bash
   pip install jupyter-notebook-mcp
   ```

## トラブルシューティング

### よくある問題

1. **テストPyPIへのアップロードが失敗する**
   - バージョン番号が既存のものと衝突していないか確認
   - APIトークンが正しく設定されているか確認

2. **インストールテストが失敗する**
   - 依存関係が正しく設定されているか確認
   - パッケージのインポートが期待通りに機能するか確認

3. **GitHub Actionsが失敗する**
   - ワークフローログを確認して具体的なエラーを特定
   - シークレット（PYPI_API_TOKEN）が正しく設定されているか確認

## バージョニング

このプロジェクトは[セマンティックバージョニング](https://semver.org/)に従います：

- **メジャーバージョン（X.0.0）**: 互換性を破る変更
- **マイナーバージョン（0.X.0）**: 後方互換性のある機能追加
- **パッチバージョン（0.0.X）**: 後方互換性のあるバグ修正 
