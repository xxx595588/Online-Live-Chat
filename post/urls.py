from django.urls import path
from . import views

urlpatterns = [
     path('post/', views.post, name='post'),
     path('getMessage/', views.getMessage, name='getMessage'),
     path('createMes/', views.createMes, name='createMes'),
]