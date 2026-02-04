from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import Group

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model= UserProfile
        fields= ['id', 'username', 'email', 'department']

""" UserProfile does NOT own passwords

Authentication is handled by django.contrib.auth.User
This serializer is not a registration serializer """

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields= ['id', 'name']
        