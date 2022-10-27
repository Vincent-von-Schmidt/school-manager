sudo apt-get update
sudo apt-get install docker.io -y
docker build -t py_app .
docker run -it -d --rm --name py_app py_app
docker run -it -d --rm -p 5432:5432 --name postgresql postgres:latest