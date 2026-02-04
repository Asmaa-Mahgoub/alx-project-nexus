from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ComponentViewSet, ComponentBatchViewSet

router= DefaultRouter()
router.register(r'components',ComponentViewSet)
router.register(r'component_batch', ComponentBatchViewSet)

urlpatterns= [
    path('', include(router.urls)),
]