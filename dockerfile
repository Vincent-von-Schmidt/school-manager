FROM python:3.10.4

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y python3-opencv libgl1-mesa-glx
RUN pip install opencv-python

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]