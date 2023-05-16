# python 3.10 alpine
FROM python:3.10-alpine

RUN pip install websockets

COPY . /app
WORKDIR /app

CMD ["python", "test.py"]