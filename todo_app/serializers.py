from rest_framework import serializers
from .models import TodoItem

from django.contrib.auth.models import User

# Create the serializers

class TodoItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TodoItem
        fields = '__all__'

# User Model Serializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']