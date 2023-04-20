from celery import shared_task

@shared_task(name='client.do')
def do(a, b):
    return a + b

@shared_task(name='client.do4')
def do4():
    return 'do 4'

@shared_task(name='client.do6')
def do6():
    return 'do 6'