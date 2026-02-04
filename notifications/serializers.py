from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='recipient.username',
        read_only=True
    )
    class Meta:
        model= Notification
        fields= '__all__'
 
     
