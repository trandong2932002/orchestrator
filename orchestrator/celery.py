from celery import Celery
from kombu.entity import Queue

app = Celery('orchestrator',
             broker='amqp://172.17.0.2',
             backend='redis://172.17.0.3',
             include=['orchestrator.tasks'])

app.conf.task_routes = {
    'orchestrator.*': {'queue': 'orchestrator'},
    'worker1.*': {'queue': 'worker1'},
    'worker2.*': {'queue': 'worker2'},
    'client.*': {'queue': 'client'},
}

app.conf.task_queues = (
    Queue('orchestrator', routing_key='default'),
)

if __name__ == '__main__':
    app.start()