kafka

Install Docker

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install docker.io

sudo apt install docker-compose

sudo apt-get update

sudo docker -v

sudo docker-compose -v

sudo docker-compose up -d

sudo docker exec -it kafka-docker bash

kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092

kafka-console-consumer.sh --topic ornek --bootstrap-server localhost:9092


Kafka kurulumu
>sudo apt-get install openjdk-8-jdk

Kafka indir
>https://archive.apache.org/dist/kafka/3.3.1/kafka_2.12-3.3.1.tgz

Zipten Çıkar
>tar -xzvf kafka_2.12-3.3.1.tgz

dizine git
>cd kafka_2.12-3.3.1/

>sudo nohup bin/zookeeper-server-start.sh config/zookeeper.properties &

>sudo nohup bin/kafka-server-start.sh config/server.properties &

>sudo bin/kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092

>sudo bin/kafka-topics.sh --delete --topic ornek --bootstrap-server localhost:9092

>sudo bin/kafka-console-consumer.sh --topic ornek --from-beginning --bootstrap-server localhost:9092

>sudo bin/kafka-console-producer.sh --topic ornek --bootstrap-server localhost:9092

