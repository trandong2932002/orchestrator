
from celery import Celery
from celery.result import allow_join_result
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

result = app.send_task('client.notify_do', (1,2), soft_time_limit=6)
result.get()
# with allow_join_result():
#     result.get()

# celery -A client.make_celery worker -l INFO
# flask run