from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    supplierName=serializers.CharField(source='supplier.supplier_name', read_only= True)
    class Meta:
        model= Order
        fields= '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    ComponentName=serializers.CharField(source='component.component_name', read_only= True)
    class Meta:
        model= OrderItem
        fields= '__all__'