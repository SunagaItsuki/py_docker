# Selenium on Docker

# 使い方
1. リポジトリをクローン

2. 以下のコマンドを実行
```
docker compose up -d
```

3. 実行するpythonスクリプト(main.py)を編集

4. 以下を実行してスクレイピング
```
docker exec py_docker-app-1 python main.py
```

※以下のURLにアクセスしてGUI画面を確認できます。(ログインパスワードはsecret)
```
http://localhost:7999/
```
