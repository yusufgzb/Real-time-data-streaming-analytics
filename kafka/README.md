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
