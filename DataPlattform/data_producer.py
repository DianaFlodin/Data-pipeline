from azure.eventhub import EventHubProducerClient, EventData
import json
import random
from datetime import datetime
import time

# Event Hub details
CONNECTION_STRING = "Endpoint=sb://inlupp1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=GGKDmIByIyyPntKSPgwRaxrI/h5DEzo9M+AEhOyOWOs="
EVENT_HUB_NAME = "dataplattforminlupp1"

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING,
    eventhub_name=EVENT_HUB_NAME
)

# Sample Data Producer
def produce_data():
    data = {
        "id": random.randint(1, 100),
        "name": random.choice(["Alice", "Bob", "Charlie", "Diana"]),
        "timestamp": datetime.now().isoformat()
    }
    return json.dumps(data)

# Send data to Event Hub
while True:
    event_data_batch = producer.create_batch()
    sample_data = produce_data()
    event_data_batch.add(EventData(sample_data))
    producer.send_batch(event_data_batch)
    print(f"Sent: {sample_data}")
    time.sleep(2)  # Simulate data production delay


    import pyodbc
from azure.eventhub import EventHubProducerClient, EventData
import json
import random
from datetime import datetime
import time

# Event Hub details
CONNECTION_STRING = "Endpoint=sb://inlupp1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=GGKDmIByIyyPntKSPgwRaxrI/h5DEzo9M+AEhOyOWOs="
EVENT_HUB_NAME = "myeventhub"

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING,
    eventhub_name=EVENT_HUB_NAME
)

# SQL Database connection details
SQL_SERVER = "dianaflodin.database.windows.net"
SQL_DATABASE = "Dianas-DB"
SQL_USERNAME = "DianaFlodin" 
SQL_PASSWORD = "2050086DF!"  

conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USERNAME};PWD={SQL_PASSWORD}'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Sample Data Producer
def produce_data():
    data = {
        "id": random.randint(1, 100),
        "name": random.choice(["Alice", "Bob", "Charlie", "Diana"]),
        "timestamp": datetime.now().isoformat()
    }
    return json.dumps(data)

# Send data to Event Hub and insert into SQL Database
while True:
    # Send data to Event Hub
    event_data_batch = producer.create_batch()
    sample_data = produce_data()
    event_data_batch.add(EventData(sample_data))
    producer.send_batch(event_data_batch)

    # Insert data into the SQL database
    data_dict = json.loads(sample_data)
    cursor.execute("INSERT INTO my_table (id, name, timestamp) VALUES (?, ?, ?)", 
                   (data_dict['id'], data_dict['name'], data_dict['timestamp']))
    conn.commit()  # Commit the transaction

    print(f"Sent to Event Hub and Inserted into DB: {sample_data}")
    time.sleep(2)  # Simulate data production delay