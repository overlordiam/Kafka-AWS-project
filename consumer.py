from kafka import KafkaConsumer
from json import loads
import json
from s3fs import S3FileSystem


consumer = KafkaConsumer("sm-producer",
                        bootstrap_servers=["3.131.85.194:9092"],
                        value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem()

for i, message in enumerate(consumer):
    with s3.open(f"s3://stock-market-analysis/stock-{i+1}.json", 'w') as file:
        json.dump(message.value, file)



    