import time
from .celery import app
from celery.exceptions import SoftTimeLimitExceeded


@app.task(name='worker1.do')
def do(data):
    try:
        data -= 1
        time.sleep(1)
        return {'status': 'SUCCESS', 'data': data}
    except SoftTimeLimitExceeded:
        return {'status': 'FAILURE'}

@app.task(name='worker1.rollback_do')
def rollback_do(data):
    try:
        data -= 1
        return {'status': 'SUCCESS', 'data': data}
    except SoftTimeLimitExceeded:
        return {'status': 'FAILURE'}