from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductComponentViewSet, ProductVersionViewSet

router= DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-components', ProductComponentViewSet)
router.register(r'product-versions', ProductVersionViewSet)

urlpatterns= [
    path('', include(router.urls)),
]