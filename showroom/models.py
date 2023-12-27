from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.functions import Now
from django_countries.fields import CountryField


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Showroom(BaseModel):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=200, null=True, choices=CountryField().choices)
    balance = models.DecimalField(max_digits=15, decimal_places=2)


class Car(BaseModel):
    production_brand = models.CharField(max_length=20)
    name = models.CharField()
    production_country = models.CharField(max_length=200, null=True, choices=CountryField().choices)
    production_year = models.IntegerField()


class CarInShowroom(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)


class Discount(BaseModel):
    percentage = models.DecimalField(max_digits=3, decimal_places=1)
    name = models.CharField(max_length=50)
    description = models.TextField()
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)
