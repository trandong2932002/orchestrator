FROM python:alpine

WORKDIR /app/worker2

RUN pip install celery redis

COPY . .

WORKDIR /app

CMD ["celery", "-A", "worker2", "worker", "-l", "INFO"]