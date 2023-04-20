import time
from .celery import app
from celery.result import allow_join_result

@app.task(name='orchestrator.do')
def do(x, y):
    # result_worker1 = app.send_task('worker1.do', (1,1))
    # with allow_join_result():
    #     print(result_worker1.get())

    notify_client1 = app.send_task('client.do4')
    with allow_join_result():
        print(notify_client1.get())

    # result_worker2 = app.send_task('worker2.do', (2,2))
    # with allow_join_result():
    #     print(result_worker2.get())

    # notify_client2 = app.send_task('client.do6')
    # with allow_join_result():
    #     print(notify_client2.get())

    return 'success'