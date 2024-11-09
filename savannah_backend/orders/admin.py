"""
Default admin Configuration for savannah/orders
"""

from django.contrib import admin
from .models import Customer, Order


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['name','code','phone']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['customer', 'item', 'amount', 'time']