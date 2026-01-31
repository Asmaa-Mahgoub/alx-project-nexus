from rest_framework import serializers
from .models import Component, ComponentBatch

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Component
        fields= '__all__'

class ComponentBatchSerializer(serializers.ModelSerializer):
    component_name = serializers.CharField(
        source='component.component_name',
        read_only=True
    )
    supplier_name = serializers.CharField(
        source='supplier.supplier_name',
        read_only=True
    )
    class Meta:
        model= ComponentBatch
        fields= '__all__'