from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, OrderItemChangeLogViewSet
from django.urls import path, include

router= DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'change-logs', OrderItemChangeLogViewSet)

urlpatterns= [
    path('',include(router.urls)),
              ]