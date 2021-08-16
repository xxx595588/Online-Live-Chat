from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register ,name='register'),
    path('account_center/', views.account_center ,name='account center'),
]