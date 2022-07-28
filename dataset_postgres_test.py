import dataset
import dotenv
import os

dotenv.load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]


# データベースに接続(なければ自動的に作成)
db = dataset.connect(DATABASE_URL)

# "address"テーブルを開く(なければ自動的に作成)
address = db["address"]

# "aaa"さんのレコードを取り出す
aaa = address.find(name="aaa")
result_aaa = list(aaa)
print(result_aaa)
print(len(result_aaa))

# レコードの追加(dictのキーによって自動的にフィールドが追加される)
address.insert({"name": "aaa", "address": "an address"})
address.insert({"name": "bbb", "address": "some address"})
address.insert({"name": "ccc", "address": "any address"})

# "aaa"さんのレコードを取り出す
aaa = address.find(name="aaa")
result_aaa = list(aaa)
print(result_aaa)
print(len(result_aaa))
