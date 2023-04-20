FROM python:alpine

WORKDIR /app/orchestrator

RUN pip install celery redis

COPY . .

WORKDIR /app

CMD ["celery", "-A", "orchestrator", "worker", "-l", "INFO"]