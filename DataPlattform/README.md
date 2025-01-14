# Data Pipeline Project

## Vad gör det här projektet?
Det här projektet är en dataintegrationspipeline som skickar data till Azure Event Hub och lagrar data i en SQL-databas.

## Installera
1. Klona repositoryt: 
    ```bash
    git clone https://github.com/DianaFlodin/Data-pipeline.git
    ```

2. Installera beroenden:
    ```bash
    pip install -r requirements.txt
    ```

3. Skapa en `.env`-fil med dina miljövariabler (se `.env.example`).

4. Kör projektet:
    ```bash
    python main.py
    ```

## Beroenden
- `pyodbc`
- `azure-eventhub`
- `python-dotenv`
