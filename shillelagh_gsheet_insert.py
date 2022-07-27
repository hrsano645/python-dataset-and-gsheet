from shillelagh.backends.apsw.db import connect

if __name__ == "__main__":
    connection = connect(
        ":memory:",
        adapter_kwargs={
            "gsheetsapi": {
                "service_account_file": "./sqlalchemy-gsheet-example-e36a52e70d5d.json",
            },
        },
    )
    cursor = connection.cursor()

    SQL = """
    SELECT *
    FROM "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=0"
    """
    for row in cursor.execute(SQL):
        print(row)

    INSERT_SQL = """
    INSERT INTO "https://docs.google.com/spreadsheets/d/1HDsGCPtamVBHhx3e_CPw1phI6RxzL_VSeC0dPUiCYBg/edit#gid=0"
    (id, name, age)
    VALUES (4, "kiki", 14);
    """

    print(cursor.execute(INSERT_SQL))
