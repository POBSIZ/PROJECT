from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='profile')

    nickname = models.CharField(max_length=20, unique=True, null=True)

    description = models.TextField(help_text="소개", null=True)
    github = models.URLField(max_length=30, null=True)
    blog = models.URLField(max_length=30, null=True)

    image = models.ImageField(help_text="대표 이미지", upload_to='profile/', null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Profiles"