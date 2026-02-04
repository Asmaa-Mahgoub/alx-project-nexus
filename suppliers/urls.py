from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SupplierViewSet, SupplierComponentViewSet

router= DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplier-component',SupplierComponentViewSet )

urlpatterns= [
    path('', include(router.urls)),
]