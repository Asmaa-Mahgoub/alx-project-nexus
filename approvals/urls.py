from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DecisionViewSet, TrialRequestViewSet

router= DefaultRouter()
router.register(r'decisions', DecisionViewSet)
router.register(r'trial-requests',TrialRequestViewSet)

urlpatterns= [
    path('', include(router.urls))
]