# マップアプリケーション

## Getting Started

### 起動前の初期設定 (Git Clone後にまずやること)
1. `.devcontainer/.env.example` を複製して `.devcontainer/.env.development` を作成する (※ リネームではなく必ず複製してください)
2. お使いのターミナルで `openssl rand -hex 32` コマンドを実行し、シークレットキーとなるランダム値を生成してください
2. 2で生成したランダムな値を `SECRET_KEY` と `TOKEN_SALT` 環境変数を設定してください。
   この際に別々の値を設定することも可能になっているので、その際は再度 `openssl rand -hex 32` コマンドを実行し、別の値を生成して設定してください。
   ```
   MYSQL_ROOT_PASSWORD=test # 任意のパスワードに変更してもいい
   MYSQL_HOST=mysql
   MYSQL_DB=map_app
   MYSQL_USER=app
   MYSQL_PASSWORD=test # 任意のパスワードに変更してもいい
   SECRET_KEY=[任意のパスワード]
   TOKEN_SALT=[任意のパスワード]
   APP_ENV=DEV
   ```

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
