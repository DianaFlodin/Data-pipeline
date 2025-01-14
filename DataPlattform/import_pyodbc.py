import pyodbc

def connect_to_db():
    try:
        connection = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=dianaflodin.database.windows.net;"
            "Database=Dianas-DB;"
            "Trusted_Connection=yes;"
        )
        return connection
    except Exception as e:
        print(f"Fel vid anslutning: {e}")
        return None
