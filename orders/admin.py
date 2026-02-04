from django.contrib import admin
from .models import Order, OrderItem, OrderItemChangeLog
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('order_no', 'order_date', 'supplier', 'status', 'expected_delivery_date',)
    search_fields=('order_no','supplier__supplier_name',)
    list_filter = ('status', 'supplier',)
    ordering=('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','component','ordered_quantity','ordered_unit','unit_price',)
    search_fields=('order__order_no','component__component_name',) #ordered_quantity is numeric → not searchable
    ordering=('component__component_name',)
    list_filter = ('ordered_unit',)

@admin.register(OrderItemChangeLog)
class OrderItemChangeLogAdmin(admin.ModelAdmin):
    list_display = (
        'order_item',
        'old_quantity',
        'new_quantity',
        'changed_by',
        'changed_at'
    )
    list_filter = ('changed_by', 'changed_at')
