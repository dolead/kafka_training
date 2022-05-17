import json
from time import sleep

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["b-1.msk-cluster-staging.fbh1vt.c9.kafka.eu-west-1.amazonaws.com:9092",
                                            "b-2.msk-cluster-staging.fbh1vt.c9.kafka.eu-west-1.amazonaws.com:9092"],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

print("Publishing 3 messages to the `MyTopic` topic on Kafka...")

for id in range(1, 4):
    my_message = {"data": "some data with ID number {}".format(str(id))}

    producer.send(topic='MSKTutorialTopic',
                  value=my_message,
                  key=b"my_key")

    sleep(5)

producer.close()
