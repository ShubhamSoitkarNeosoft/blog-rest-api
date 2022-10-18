from app import celery


@celery.task()
def add_together(a, b):
    print("inside celery task")
    return a + b

result = add_together.delay(23, 42)
result.wait()