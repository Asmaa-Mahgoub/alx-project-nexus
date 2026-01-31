from rest_framework import serializers
from .models import Product, ProductComponent, ProductVersion

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

class ProductComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductComponent
        fields= '__all__'

    class ProductVersionSerializer(serializers.ModelSerializer):
        product_name= serializers.CharField(source= 'product.name', read_only =True)
        class Meta:
            model= ProductVersion
            fields= '__all__'