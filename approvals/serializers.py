from rest_framework import serializers
from .models import TrialRequest,Decision

class TrialRequestSerializer(serializers.ModelSerializer):
    requested_by_name = serializers.CharField(
        source='requested_by.username',
        read_only=True
    )
    product_name = serializers.CharField(
        source='version.product.name',
        read_only=True
    )
    version_no = serializers.CharField(
        source='version.version_no',
        read_only=True
    )
    class Meta:
        model= TrialRequest
        fields= '__all__'

class DecisionSerializer(serializers.ModelSerializer):
    decided_by_name = serializers.CharField(
        source='decided_by.username',
        read_only=True
    )
    decision_label = serializers.CharField(
        source='get_decision_display',   
        read_only=True
    )
    class Meta:
        model= Decision
        fields= '__all__'
"""get_<field>_display is GOLD for TextChoices"""