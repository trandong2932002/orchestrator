import time
from datetime import datetime
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded
from celery.result import allow_join_result
from flask import current_app
from marshmallow import Schema, fields

# this function do not need to decorate with @shared_task,
# because it is not a distributed task,
# it is only called by this app 
def do(data):
    print('client.do')
    # do something
    data -= 1
    result = current_app.extensions['celery'].send_task('orchestrator.do', (data,))
    result.get() # wait for result
    # this func dont care return anything
    # because orchestrator make sure the distributed transaction success or fail
    # it only need to care about it have to wait until the d-transaction have done
    # before create a response to user 
    return

@shared_task(name='client.notify_do')
def notify_do(data, worker_id):
    try:
        print('notify_do', data)
        print(worker_id, 'done')
        return {'status': 'SUCCESS', 'data': data}
    except SoftTimeLimitExceeded:
        return {'status': 'TIMEOUT'}

@shared_task(name='client.rollback_do')
def rollback_do(data):
    try:
        print('rollback_do')
        return {'status': 'SUCCESS', 'data': data}
    except SoftTimeLimitExceeded:
        return {'status': 'TIMEOUT'}