from celery import Celery, shared_task


@shared_task
def customer_purchase():
    print("customer task complete")
