FROM python:alpine

WORKDIR /app/worker1

RUN pip install celery redis

COPY . .

WORKDIR /app

CMD ["celery", "-A", "worker1", "worker", "-l", "INFO"]