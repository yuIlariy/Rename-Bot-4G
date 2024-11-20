
FROM python:latest

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 bot.py