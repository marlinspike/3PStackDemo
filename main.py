import time
import os
import uuid
import datetime
import random
import json
from dotenv import load_dotenv

load_dotenv()
EHUB_CON_STR = os.getenv("EHUB_CON_STR")
from azure.eventhub import EventHubProducerClient, EventData

devices = []
for x in range(0, 2):
    devices.append(str(uuid.uuid4()))

    producer = EventHubProducerClient.from_connection_string(
        conn_str=f"{EHUB_CON_STR}"
    )
countries = [
    "Germany",
    "Italy",
    "Canada",
    "France",
    "United Kingdom"
    "Australia",
    "Spain",
    "India",
    "Australia"
]

for y in range(0, 200):
    event_data_batch = producer.create_batch()

    for dev in devices:
        reading = {
            "id": dev,
            "country": countries[random.randrange(0, 8)],
            "timestamp": str(datetime.datetime.utcnow()),
            "value01": random.random(),
            "value02": random.randint(10, 100),
            "value03": random.randint(500, 1000),
        }

        s = json.dumps(reading)
        print(s)
        event_data_batch.add(EventData(s))
    producer.send_batch(event_data_batch)
    time.sleep(10)
producer.close()