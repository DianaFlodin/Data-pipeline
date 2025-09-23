import pyodbc

SQL_SERVER = "dianaflodin.database.windows.net"
SQL_DATABASE = "Dianas-DB"
SQL_USERNAME = "DianaFlodin" 
SQL_PASSWORD = "2050086DF!"  

def connect_to_db():
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USERNAME};PWD={SQL_PASSWORD}'
    connection = pyodbc.connect(conn_str)
    return connection

def fetch_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 name, event_timestamp FROM mytable ORDER BY event_timestamp DESC")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Namn: {row.name}, Tid: {row.event_timestamp}")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_data()
