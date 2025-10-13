from django.db import models
from django.contrib.auth.models import User
# description, creator

class Event(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
