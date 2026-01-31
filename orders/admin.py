from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('order_no', 'order_date', 'supplier', 'status', 'expected_delivery_date')
    search_fields=('order_no','supplier__supplier_name')
    list_filter = ('status', 'supplier')
    ordering=('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','component','ordered_quantity','ordered_unit','unit_price')
    search_fields=('order__order_no','component__component_name') #ordered_quantity is numeric → not searchable
    ordering=('Component__component',)
    list_filter = ('ordered_unit',)