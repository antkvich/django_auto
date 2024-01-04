from django.contrib.auth.models import User
from django.db import models

from showroom.models import BaseModel, Car, Showroom


class Customer(BaseModel):
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)


class PurchaseOffer(BaseModel):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=15, decimal_places=2)


class Purchase(BaseModel):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    showroom = models.ForeignKey(Showroom, on_delete=models.PROTECT)
