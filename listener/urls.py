from django.urls import path

from .views import ConnectionsViews

urlpatterns = [
    path('', ConnectionsViews.as_view(), name='socket connections'),
]