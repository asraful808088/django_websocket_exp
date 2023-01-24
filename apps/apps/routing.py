from django.urls import path

from .consumers import ChatWebsocket

urlspatterns = [
    path('ws/ac',ChatWebsocket.as_asgi())
]