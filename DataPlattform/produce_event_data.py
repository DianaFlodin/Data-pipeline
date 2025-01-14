import random
import json
from datetime import datetime

def generate_event_data():
    event_data = {
        "event_id": random.randint(1000, 9999),
        "event_type": "UserLogin",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": {
            "user_id": random.randint(1, 100),
            "username": f"user{random.randint(1, 100)}"
        },
        "details": {
            "ip_address": f"192.168.0.{random.randint(1, 255)}",
            "location": "Stockholm, Sweden"
        }
    }
    
    # Konvertera till JSON-format
    return json.dumps(event_data, indent=4)
