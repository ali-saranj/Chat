from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chat
from .serializers import ChatSerializers


# Create your views here.
@api_view(["GET"])
def showChat(request):
    chat = Chat.objects.all()
    chatsel = ChatSerializers(chat, many=True)
    return Response(chatsel.data)


@api_view(["POST"])
def addChat(request):
    a = dict(request.data)
    chat = ChatSerializers(data=a)

    if chat.is_valid():
        chat.save()
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "cansel"})
