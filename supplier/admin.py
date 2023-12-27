from django.contrib import admin

from supplier.models import LoyaltySupplierDiscount, Supplier, SupplierCar, SupplierSales, SuppliersDiscount


admin.site.register(Supplier)
admin.site.register(SupplierCar)
admin.site.register(LoyaltySupplierDiscount)
admin.site.register(SupplierSales)
admin.site.register(SuppliersDiscount)
