from rest_framework import viewsets
from .models import Component,  ComponentBatch
from .serializers import ComponentSerializer, ComponentBatchSerializer
from rest_framework.decorators import action

# Create your views here.
class ComponentViewSet(viewsets.ModelViewSet):
    queryset= Component.objects.all()
    serializer_class= ComponentSerializer

class ComponentBatchViewSet(viewsets.ModelViewSet):
    queryset= ComponentBatch.objects.all()
    serializer_class= ComponentBatchSerializer