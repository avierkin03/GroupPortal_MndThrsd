from django.db import models

# description, creator

class h():
    title = models.CharField(max_length=100)
    user = models.ForeignKey()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
