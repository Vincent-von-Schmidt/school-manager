sudo apt-get update
sudo apt-get install docker.io -y
docker build -t py_app .
docker run -it --rm --name py_app py_app