from django.contrib import admin

from showroom.models import Car, CarInShowroom, Discount, Showroom


admin.site.register(Car)
admin.site.register(Showroom)
admin.site.register(CarInShowroom)
admin.site.register(Discount)
