import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=["3.131.85.194:9092"],
                         value_serializer=lambda x: dumps(x).encode("utf-8"))


df = pd.read_csv("indexProcessed.csv")
# print(df.head())
# print(df.sample(1).to_dict(orient="records")[0])

while True:
    stock = df.sample(1).to_dict(orient="records")[0]
    producer.send("sm-producer", value=stock)
    sleep(2)

