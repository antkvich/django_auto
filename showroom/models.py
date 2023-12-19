from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.functions import Now
from django_countries.fields import CountryField


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=Now())


class Showroom(BaseModel):
    name = models.CharField(max_length=50)
    country = CountryField()
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    max_car_year = models.IntegerField(max_length=4, null=True)
    min_car_year = models.IntegerField(max_length=4, null=True)
    allowed_brands = ArrayField(models.CharField(max_length=30), null=True)
    allowed_countries = ArrayField(CountryField(), null=True)


class Car(BaseModel):
    production_brand = models.CharField(max_length=20)
    name = models.CharField()
    production_country = CountryField()
    production_year = models.IntegerField(max_length=4)


class CarInShowroom(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    mileage = models.DecimalField(max_digits=8, decimal_places=1)


class Discount(BaseModel):
    percentage = models.DecimalField(max_digits=3, decimal_places=1)
    name = models.CharField(max_length=50)
    description = models.TextField()
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)
