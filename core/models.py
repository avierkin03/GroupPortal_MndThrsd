from django.db import models
from django.contrib.auth.models import User

# Модель "Профіль групи"
class GroupProfile(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='group_logos/', blank=True, null=True)
    created_time= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Модель "Профіль користувача"
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('moderator', 'Moderator'),
        ('member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
