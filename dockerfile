FROM python:3.11.0

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y python3-opencv libgl1-mesa-glx libegl1 libx11-xcb1
RUN pip install opencv-python

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/main.py" ]
