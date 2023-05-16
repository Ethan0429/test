# python 3.10 alpine
FROM python:3.10-alpine

COPY . /app
WORKDIR /app

CMD ["python", "test.py"]