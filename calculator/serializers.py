from rest_framework import serializers
from .models import Calculate

class CalculateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculate
        fields = '__all__'
