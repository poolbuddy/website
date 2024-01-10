# serializers.py
from djoser.serializers import UserCreateSerializer
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'date_joined' ] 


class CustomUserCreateSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'date_joined', 'last_login' )

    def create(self, validated_data):

        user = super().create(validated_data)

        return user
