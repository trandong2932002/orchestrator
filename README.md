# Orchestrator

## Description

service 1 = client  
service 2 = worker1  
service 3 = worker2  
<service n = worker n (optional)>  
orchestrator  

| do          | service 1    | -> | service 2    | -> | service 3    |
|-------------|--------------|----|--------------|----|--------------|
| fail        | rollback     |    |              |    |              |
| fail        | rollback     | <- | rollback     |    |              |
| fail        | rollback     | <- | rollback     | <- | rollback     |
| success     | complete 1   |    |              |    |              |
| success     | complete 2   | <- | 2 success    |    |              |
| success     | complete all |    |              | <- | 3 success    |


## Build

In worker1, worker2, orchestrator directories, type
```
docker buildx build -t <worker1/worker2/orchestrator> .
```

## Run

### For worker1, worker2, orchestrator

```
docker run --rm <worker1/worker2/orchestrator>
```

### For client

In client directory, run flask app
```
flask run
```

In root directory, run client celery
```
celery -A client.make_celery worker -l INFO
```