from django.contrib import admin
from .models import Component, ComponentBatch
# Register your models here.

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display= ('component_name')
    search_fields= ('component_name')
    ordering= ('component_name')


@admin.register(ComponentBatch)
class ComponentBatchAdmin(admin.ModelAdmin):
    list_display= ('component','supplier', 'quantity', 'batch_no', 'expiry_date', 'received_date', 'created_at','status')
    search_fields=('component__component_name','supplier__supplier_name','batch_no')
    list_filter = ('status', 'supplier')
    ordering=('-expiry_date',)