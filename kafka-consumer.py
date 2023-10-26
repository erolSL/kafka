from kafka import KafkaConsumer
import json
import mysql


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "test",
        bootstrap_servers=['192.168.1.3:9092'],
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
    )
    print("okumaya başlıyoruz")

    for msg in consumer:
        veri = json.loads(msg.value)
        print("Data: {}".format(veri))
        print("{} ismi {} karakterden oluşuyor.".format(veri['name'], len(veri['name'])))

# name
# address
# create_at