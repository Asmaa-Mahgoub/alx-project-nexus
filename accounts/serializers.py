from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User

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
