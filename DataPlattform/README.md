# Dataplattformar och molnlösningar – Data Pipeline Project

## Projektbeskrivning
Detta projekt är en dataintegrationspipeline som producerar data lokalt med Python, skickar data till Azure Event Hub och lagrar det i en serverless SQL-databas. Projektet innehåller även konsumenter (Python-script) som hämtar och visar data från databasen.

## Funktioner
- **Dataproducent:** Genererar och skickar data med Python till Azure Event Hub.
- **Databaslagring:** Sparar data i Azure SQL Database (serverless).
- **Datakonsumenter:** Två olika Python-script som konsumerar och visar data.
- **Säkerhet:** Miljövariabler och känslig information hanteras via `.env` (ej uppladdad).
- **Grafana:** Ursprungsplanen var att använda Grafana, men detta valdes bort då det medförde kostnader. Konsumering och visualisering sker istället med Python.

## Kom igång

### 1. Klona repositoryt
```bash
git clone https://github.com/DianaFlodin/Data-pipeline.git
```

### 2. Installera beroenden
```bash
pip install -r requirements.txt
```

### 3. Skapa en .env-fil
Lägg dina connection strings och känsliga uppgifter i en `.env`-fil (se `.env.example`).  
**OBS!** `.env` laddas **inte** upp till GitHub.

### 4. Kör programmet
Starta huvudprogrammet:
```bash
python main.py
```
eller
```bash
python import_pyodbc.py
```
beroende på vilket script du vill köra.

### 5. Konsumera data
Använd de medföljande Python-scripten för att hämta och visa data från databasen.

## Viktiga filer
- `import_pyodbc.py` – Producerar, skickar och lagrar data i Azure.
- `main.py` – Sammanställer och kör delar av projektet.
- `.gitignore` – Ignorerar känsliga och temporära filer.
- `requirements.txt` – Lista över Python-paket.
- `README.md` – Denna fil.
- `.env.example` – Exempel på miljövariabler.

## Beroenden
- pyodbc
- azure-eventhub
- python-dotenv

## Kommentar om Grafana
Grafana användes inte på grund av kostnad. Konsumering och visualisering visas istället med Python-script.

## Kontakt
Diana Flodin  
Kurs: Dataplattformar och molnlösningar
