FROM jaspesoft/python-alpine-grpcio

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install --upgrade pip && pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

ARG GOOGLE_CREDENTIALS=""

RUN echo $GOOGLE_CREDENTIALS > /credentials.json

ENV GOOGLE_APPLICATION_CREDENTIALS="/credentials.json"

COPY . .

CMD ["python", "-u", "./service.py"]
