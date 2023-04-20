
from celery import Celery
app = Celery(broker='amqp://localhost',backend='redis://localhost')

# app.conf.task_routes = {
#     'add.*': {'queue': 'add'}, 
#     'mul.*': {'queue': 'mul'}, 
# }
# app.send_task('add.add', (2,2))

# app.send_task('mul.mul', (2,2))


# app.conf.task_routes = {
#     'worker1.*': {'queue': 'worker1'},
# }

# app.send_task('orchestrator.do', (2,2))


app.conf.task_routes = {
    'client.*': {'queue': 'client'},
}

app.send_task('client.do6',)


# celery -A client.make_celery worker -l INFO
# flask run