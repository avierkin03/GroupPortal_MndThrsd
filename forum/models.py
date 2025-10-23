from django.db import models
from django.contrib.auth.models import User

#Тема опитування
class Topic(models.Model):
    title = models.CharField(max_length=200)
    descripton = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topic_creator")
    created_time = models.DateTimeField(auto_now_add=True)

#Пост користувача в якомусь опитуванні
class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_creator")
    created_time = models.DateTimeField(auto_now_add=True)