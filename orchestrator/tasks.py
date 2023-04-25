from .celery import app
from celery.result import allow_join_result


NUM_WORKER = 2 # determine by bussiness process and number of services

#* <do> should be the name of the action: transfer, withdraw, ...

#* ORCHESTRATOR
@app.task(name='orchestrator.do')
def do(data):
    # after receive request to make a transaction
    # worker do all local transactions
    for worker_id in range(1, NUM_WORKER + 1):
        do_result = worker_do(data, worker_id)
        # if one of local transactions is fail or timeout, rollback
        if do_result['status'] == 'TIMEOUT':
            # rollback all complete worker and client
            for j in range(1, worker_id):
                worker_rollback_do(data, j)
            client_rollback_do(data)
            return {'status': 'FAILURE'}
        # if this local transaction done, notify to the client
        # that make a transaction to update a status of distributed transaction
        #
        data = do_result['data']
        print(data)
        #
        client_notify_do(data, worker_id)

    return {'status': 'SUCCESS'}

# -----------------------------------------------------------------
#* DO
def worker_do(data, worker_id):
    result = app.send_task(f'worker{worker_id}.do', (data,))
    with allow_join_result():
        return result.get()

#* ROLLBACK = CLIENT + n x WORKER
def worker_rollback_do(data, worker_id):
    result = app.send_task(f'worker{worker_id}.rollback_do', (data,))
    with allow_join_result():
        return result.get()

def client_rollback_do(data):
    result = app.send_task('client.rollback_do', (data,))
    with allow_join_result():
        return result.get()

#* COMPLETE NOFIFY
def client_notify_do(data, worker_id): # worker_id done its work
    result = app.send_task('client.notify_do', (data, worker_id))
    with allow_join_result():
        return result.get()