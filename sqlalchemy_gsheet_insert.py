from sqlalchemy.engine import create_engine

engine = create_engine(
    "gsheets://",
    catalog={
        "user": "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=0",
        "accesslog": "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=1070707997",
    },
    service_account_file="./credential.json",
)
connection = engine.connect()
result = connection.execute("SELECT * FROM user")
for row in result:
    print(row)
result = connection.execute("SELECT * FROM accesslog")
for row in result:
    print(row)

query = "INSERT INTO user VALUES (?, ?, ?)"
connection.execute(query, (4, "kiki", 10))
connection.execute(query, (5, "aya", 15))

result = connection.execute("SELECT * FROM user")
for row in result:
    print(row)
