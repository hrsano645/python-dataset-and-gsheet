import dataset

# データベースに接続(なければ自動的に作成)
db = dataset.connect(
    "gsheets://",
    engine_kwargs={
        "catalog": {
            "users": "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=0",
            "accesslog": "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=1070707997",
        },
        "service_account_file": "./credential.json",
    },
)

# "address"テーブルを開く(なければ自動的に作成)
for user in db["users"]:
    print(user)
for logline in db["accesslog"]:
    print(logline)
