import time
from kafka import KafkaProducer
import json
from data import get_user


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['192.168.1.3:9092'],
                         value_serializer=json_serializer)


if __name__ == "__main__":
    print("yazmaya başlıyoruz.")
    while True:
        user = get_user()
        print(user)
        producer.send("test", user)
        time.sleep(5)

