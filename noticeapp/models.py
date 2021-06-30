from django.db import models

from froala_editor.fields import FroalaField
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Notice(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='notice')

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notice_thumbnail/', null=True, blank=True)

    content = FroalaField(plugins=('font_size', 'font_family'), null=True, blank=True, options={
        'toolbarInline': True,
    })

    created_at = models.DateField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
