from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, GroupViewSet

router= DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns=[
    path('', include(router.urls))
]