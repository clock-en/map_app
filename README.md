# マップアプリケーション

## Getting Started

### Dockerの起動 (VScode devcontainer を使用)
1. VScodeに `Remote Development` をインストールする (ms-vscode-remote.vscode-remote-extensionpack)
2. リポジトリをclone
3. cloneしたディレクトリに移動してVScodeで開く
4. VScode画面左下にある 緑色の`><`マークをクリック
5. 上部に表示されたパレットから `Open Folder in Container...` を選択

上記ステップを踏むことでDocker Containerを生成してその中でコーディングできるようになります。

### アプリケーションの起動
1. 起動後のVScodeターミナルで `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload` を実行
2. ブラウザで `http://localhost:8000` にアクセス
