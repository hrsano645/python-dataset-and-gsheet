import re
from sqlalchemy.engine import create_engine

engine = create_engine(
    "gsheets://",
    # catalog={
    #     "user": "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=0",
    #     "accesslog": "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=1070707997",
    # },
    service_account_file="./credential.json",
)
connection = engine.connect()

query = "CREATE TABLE a_table (A int, B string)"
result = connection.execute(query)
print(result.rowcount)
