import dataset

# データベースに接続(なければ自動的に作成)
db = dataset.connect("sqlite:///test.sqlite")

# "address"テーブルを開く(なければ自動的に作成)
address = db["address"]

# レコードの追加(dictのキーによって自動的にフィールドが追加される)
address.insert({"name":"aaa", "address": "an address"})
address.insert({"name":"bbb", "address": "some address"})
address.insert({"name":"ccc", "address": "any address"})

# "aaa"さんのレコードを取り出す
aaa = address.find_one(name="aaa")
print(aaa)