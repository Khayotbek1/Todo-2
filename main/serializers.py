from rest_framework import serializers
from .models import *
from accounts.serializers import AccountUpdateSerializer

class PlanSerializer(serializers.ModelSerializer):
    user = AccountUpdateSerializer(read_only=True, many=False)
    class Meta:
        model = Plan
        fields = '__all__'


class PlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True},
            'status': {'read_only': True},
        }

class PlanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }