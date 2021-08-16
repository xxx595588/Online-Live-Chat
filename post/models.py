from django.db import models
from account.models import Account
from datetime import datetime

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='post', null=True)
    authorname = models.CharField(max_length=100, default='xxx595588')
    text = models.CharField(max_length=100)
    send_at = models.DateTimeField(default=datetime.now)
    #like = models.IntegerField(default=0)