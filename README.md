# 食品管理アプリ

## Docker起動方法
1. ディレクトリを移動する
```
cd expriy_management
```

2. Dockerを起動する
コンテナをビルド
```
docker-compose build --no-cache
```

コンテナを起動
```
docker-compose up -d
```

3.  <http://localhost:5000> を確認

## DB接続方法
```
docker-compose exec db mysql -u root -p
```
パスワードを入力後、sqlコマンドが使用可能
```
exit
```
で終了

## 作業終了時
Dockerを終了する
```
docker-compose down
```
