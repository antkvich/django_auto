from django.contrib.postgres.fields import ArrayField
from django.db import models

from showroom.models import BaseModel, Car, Showroom


class Customer(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    email = models.EmailField()
    username = models.CharField(max_length=30)


class PurchaseOffer(BaseModel):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=15, decimal_places=2)
    color = models.CharField(max_length=20, blank=True)


class Purchase(BaseModel):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    showroom = models.ForeignKey(Showroom, on_delete=models.PROTECT)
