from rest_framework import serializers
from .models import User , Data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields =  ['amount', 'date', 'description', 'category']

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields =  '__all__'