import json
from kafka import KafkaProducer
import pandas as pd
import time

server = "35.222.63.42:9092"
topic_name = "ornek"

producer = KafkaProducer(
    bootstrap_servers=server,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

df = pd.read_csv("c876bd01.csv")

for _, row in df.iterrows():
    to_json = row.to_dict()
    print("veri gönderiliyor")
    producer.send("ornek", value=to_json)
    producer.flush()

producer.close()
