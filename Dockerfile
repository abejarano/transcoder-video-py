FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./

RUN apk add linux-headers && apk update && apk add ffmpeg make gcc g++

RUN pip3 install --upgrade pip && pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./service.py"]