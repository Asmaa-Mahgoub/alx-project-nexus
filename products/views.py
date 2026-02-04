from rest_framework import viewsets
from .models import Product, ProductComponent, ProductVersion
from .serializers import ProductSerializer, ProductComponentSerializer, ProductVersionSerializer
from rest_framework.decorators import action

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

class ProductComponentViewSet(viewsets.ModelViewSet):
    queryset= ProductComponent.objects.all()
    serializer_class= ProductComponentSerializer

class ProductVersionViewSet(viewsets.ModelViewSet):
    queryset= ProductVersion.objects.all()
    serializer_class= ProductVersionSerializer