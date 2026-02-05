from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    department = serializers.ChoiceField(choices=UserProfile.Department.choices)

    def create(self, validated_data):
        password = validated_data.pop('password')
        department = validated_data.pop('department')

        user = User.objects.create_user(
            **validated_data,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            department=department
        )

        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data['user'] = user
        return data