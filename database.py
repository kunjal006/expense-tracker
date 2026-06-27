import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname = "expense_tracker",
        user = "postgres",
        password = "bhavya",
        host = "localhost",
        port = "5432"
    )
    return conn