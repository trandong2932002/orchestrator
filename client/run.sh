#!/bin/bash
nohup flask run > flask_run.out 2>&1 &

cd ..
nohup celery -A client.make_celery worker -l INFO & > celery 2>&1 &