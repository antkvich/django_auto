from django.db import models
from django.db.models.functions import Now
from django_countries.fields import CountryField


class Showroom(models.Model):
    name = models.CharField(max_length=50)
    country = CountryField()
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(db_default=Now())
    max_car_year = models.IntegerField(max_length=4, null=True)
    min_car_year = models.IntegerField(max_length=4, null=True)


class Car(models.Model):
    name = models.CharField()
    production_country = CountryField()
    is_active = models.BooleanField(default=True)
    production_year = models.IntegerField(max_length=4)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)


class Discount(models.Model):
    percentage = models.DecimalField(max_digits=3, decimal_places=1)
    name = models.CharField(max_length=50)
    description = models.TextField()
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)
    is_active = models.BooleanField(default=True)


class AllowedCarBrand(models.Model):
    name = models.CharField(max_length=30)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)


class AllowedCarCountry(models.Model):
    country = CountryField()
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)





