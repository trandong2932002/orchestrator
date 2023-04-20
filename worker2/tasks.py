import time
from .celery import app


@app.task(name='worker2.do')
def do(x, y):
    time.sleep(1)
    return x + y
