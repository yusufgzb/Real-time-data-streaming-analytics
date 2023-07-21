airflow

Install Docker

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install docker.io

sudo apt install docker-compose

sudo apt-get update

sudo docker -v

sudo docker-compose -v

---

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up airflow-init

sudo docker-compose up -d
