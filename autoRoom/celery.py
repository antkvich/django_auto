import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autoRoom.settings")


app = Celery("autoRoom", broker="redis://redis:6379/0")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(["customer", "showroom"])
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    "customer-purchase-task": {
        "task": "customer.tasks.customer_purchase",
        "schedule": 10.0,
    },
    "showroom-purchase-task": {
        "task": "showroom.tasks.showroom_purchase",
        "schedule": 5.0,
    },
}

if __name__ == "__main__":
    app.start()
