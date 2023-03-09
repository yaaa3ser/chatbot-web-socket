from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Chat
        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
    