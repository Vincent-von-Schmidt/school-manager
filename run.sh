sudo apt-get update
sudo apt-get install docker.io -y

docker build -t py_app .
docker run -it -d --rm --name py_app py_app

docker run -it -d --rm -p 5432:5432 -e POSTGRES_PASSWORD=1234 --name postgresql postgres:latest

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE school;
EOSQL

dump = $(cat ./database_dump_postgresql.sql)

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "school" <<-EOSQL
    $dump
EOSQL