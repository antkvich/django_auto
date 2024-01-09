from celery import shared_task


@shared_task
def showroom_purchase():
    print("showroom task complete")
