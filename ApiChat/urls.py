
from django.urls import path

from . import views

urlpatterns = [
    path('showChat', views.showChat, name='showChat'),
    path('addChat', views.addChat, name='addChat'),
]

