import produce_event_data
import import_pyodbc

def main():
    print("Startar programmet...")
    
    # Här kan du kalla på funktioner från de andra modulerna
    event_data = produce_event_data.generate_event_data()  # En funktion från produce_event_data.py
    print(event_data)
    
    # Databasanslutning med hjälp av pyodbc
    connection = import_pyodbc.connect_to_db()
    print("Ansluten till databas:", connection)

if __name__ == "__main__":
    main()
