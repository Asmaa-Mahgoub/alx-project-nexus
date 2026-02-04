from rest_framework import serializers
from .models import Supplier, SupplierComponent

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model= Supplier
        fields= '__all__'

class SupplierComponentSerializer(serializers.ModelSerializer):
        class Meta:
            model= SupplierComponent
            fields= '__all__'