from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from rest_framework import viewsets
from .models import Supplier, SupplierComponent
from .serializers import SupplierSerializer, SupplierComponentSerializer
from rest_framework.decorators import action

# Create your views here.

class SupplierViewSet(viewsets.ModelViewSet):
    queryset= Supplier.objects.all()
    serializer_class= SupplierSerializer

class SupplierComponentViewSet(viewsets.ModelViewSet):
    queryset= SupplierComponent.objects.all()
    serializer_class= SupplierComponentSerializer