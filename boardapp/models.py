from django.db import models

from froala_editor.fields import FroalaField
from django.conf import settings
from hitcount.models import HitCountMixin

User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model, HitCountMixin):

    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='post')

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_thumbnail/', null=True, blank=True)

    content = FroalaField(plugins=('font_size', 'font_family'), null=True, blank=True, options={
        'toolbarInline': True,
    })
    
    watches = models.PositiveIntegerField(default=0, verbose_name="조회수")

    created_at = models.DateField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
