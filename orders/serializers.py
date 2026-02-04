from rest_framework import serializers
from .models import Order, OrderItem, OrderItemChangeLog

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
        
class OrderQuantityUpdateSerializer(serializers.Serializer):
    order_item_id = serializers.IntegerField()
    new_quantity = serializers.DecimalField(max_digits=10, decimal_places=3)
    reason = serializers.CharField(required=False)

class OrderItemChangeLogSerializer(serializers.Serializer):
      changed_by_username = serializers.CharField(
        source='changed_by.username',
        read_only=True
    )
      class Meta:
        model= OrderItemChangeLog
        fields= '__all__'