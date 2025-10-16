from django.contrib import admin
from .models import GroupProfile, UserProfile

admin.site.register(UserProfile)
admin.site.register(GroupProfile)