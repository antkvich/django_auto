from django.db import models

from showroom.models import BaseModel, Car, Showroom


class Supplier(BaseModel):
    name = models.CharField(max_length=50)


class SupplierCar(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class SuppliersDiscount(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=3, decimal_places=1)


class LoyaltySupplierDiscount(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=3, decimal_places=1)
    purchases_required = models.IntegerField()


class SupplierSales(BaseModel):
    car = models.ForeignKey(SupplierCar, on_delete=models.PROTECT)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
