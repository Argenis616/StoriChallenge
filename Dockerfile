FROM python:3.9-slim AS builder

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN rm -rf awscliv2.zip ./aws

FROM python:3.9-slim

COPY credentials /root/.aws/credentials

RUN chmod 600 /root/.aws/credentials

WORKDIR /app

COPY app /app
COPY requirements.txt /app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--limit-concurrency", "300"]
