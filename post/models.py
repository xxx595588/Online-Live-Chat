from django.db import models
from account.models import Account
#from datetime import datetime

# Create your models here.

class Chatroom(models.Model):
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='chatroom', null=True)
    creator = models.CharField(max_length=100)
    room_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='post_auth', null=True)
    room = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='post_room', null=True)
    roomname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    send_at = models.DateTimeField(auto_now_add=True)