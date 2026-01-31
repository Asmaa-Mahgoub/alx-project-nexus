from django.contrib import admin
from .models import Supplier, SupplierComponent
# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display=('supplier_name','email', 'shipment_method')
    search_fields=('supplier_name','shipment_method')

@admin.register(SupplierComponent)
class SupplierComponentAdmin(admin.ModelAdmin):
    list_display=('supplier','component','minimum_order_quantity', 'unit_price','expected_delivery_period')
    search_fields=('supplier__supplier_name','component__component_name')
    list_filter = ('supplier')