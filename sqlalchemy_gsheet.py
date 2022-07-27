from sqlalchemy.engine import create_engine

engine = create_engine(
    "gsheets://",
    {"catalog": {
        "simple_sheet": "https://docs.google.com/spreadsheets/d/1_rN3lm0R_bU3NemO0s9pbFkY5LQPcuy1pscv8ZXPtg8/edit#gid=0",
    },}
)


connection = engine.connect()
connection.execute("SELECT * FROM simple_sheet")