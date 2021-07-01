from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from boardapp.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)
