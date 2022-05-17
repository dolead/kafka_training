from kafka import KafkaConsumer

my_consumer = KafkaConsumer('MSKTutorialTopic',
                            bootstrap_servers=["b-1.msk-cluster-staging.fbh1vt.c9.kafka.eu-west-1.amazonaws.com:9092",
                                               "b-2.msk-cluster-staging.fbh1vt.c9.kafka.eu-west-1.amazonaws.com:9092"])

print("Listening for incoming messages...", "\n")

for record in my_consumer:
    print("Consumer Object : ", record, "\n")
    print("Data : ", record.value, "\n")

my_consumer.close()
