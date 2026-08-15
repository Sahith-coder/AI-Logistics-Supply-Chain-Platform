from django.contrib import admin
from .models import User, Warehouse, Customer, Driver, Vehicle, Order, Assignment


admin.site.register(User)
admin.site.register(Warehouse)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(Assignment)