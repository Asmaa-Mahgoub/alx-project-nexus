from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer, GroupSerializer
from django.contrib.auth.models import Group
 

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    #❌queryset= UserProfile.objects.all() GET /api/users/  → returns everyone
    serializer_class= UserProfileSerializer
    
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

""" ReadOnlyModelViewSet: This is a security choice. It only allows GET requests (list and retrieve). 
It prevents hackers from using your API to create new groups like "Super-Hacker" or deleting your "Director" group. """