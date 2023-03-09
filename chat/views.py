from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializer
from rest_framework import status
from django.shortcuts import render
from .models import Chat


class ChatView(APIView):
    def get(self, request):
        chats = Chat.objects.all()
        data = ChatSerializer(chats, many=True)
        return render(request, 'chat/chat.html', {'data': data.data})
    
    