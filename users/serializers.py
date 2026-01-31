from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields= '__all__'

""" UserProfile does NOT own passwords

Authentication is handled by django.contrib.auth.User
This serializer is not a registration serializer """