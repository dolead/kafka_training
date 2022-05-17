from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin_client = KafkaAdminClient(bootstrap_servers=["b-1.msk-cluster-staging.fbh1vt.c9.kafka.eu-west-1.amazonaws.com:9092",
                                               "b-2.msk-cluster-staging.fbh1vt.c9.kafka.eu-west-1.amazonaws.com:9092"])
admin_client.delete_topics(["MyTopic"])

topics = admin_client.list_topics()

# admin_client.create_topics(new_topics=[NewTopic("MyTopic", num_partitions=1, replication_factor=1)])
