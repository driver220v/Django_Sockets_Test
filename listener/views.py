from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.generics import GenericAPIView


class ConnectionsViews(View):
    def get(self):
        pass