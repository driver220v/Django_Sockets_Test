from django.urls import path

from .views import ConnectionsViews

urlpatterns = [
    path('conn/', ConnectionsViews.as_view(), name='socket connections'),
]