from celery import Celery
from kombu.entity import Queue

app = Celery('worker1',
             broker='amqp://172.17.0.2',
             backend='redis://172.17.0.3',
             include=['worker1.tasks'])

app.conf.task_queues = (
    Queue('worker1', routing_key='default'),
)

if __name__ == '__main__':
    app.start()