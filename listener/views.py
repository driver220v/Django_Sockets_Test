from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from rest_framework.generics import GenericAPIView

from Django_Sockets_Test.listener.consumer import SocketConnection


class ConnectionsViews(TemplateView):
    template_name = 'listener/index.html'
