from django.contrib import admin

from customer.models import Customer, Purchase, PurchaseOffer


admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(PurchaseOffer)
