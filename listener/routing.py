from Django_Sockets_Test.listener import consumer
from django.urls import path


websocket_urlpatterns = [
    path('ws/conn/', consumer.SocketConnection)
]