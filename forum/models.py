from django.db import models
from django.contrib.auth.models import User

#Тема опитування
class Topic(models.Model):
    title = models.CharField(max_length=200)
    descripton = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")
    created_time = models.DateTimeField()

#Пост користувача в якомусь опитуванні
class Post(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_time = models.DateTimeField()