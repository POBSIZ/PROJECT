from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)
    description = models.TextField(help_text="소개", null=True)
    github = models.URLField(max_length=30, null=True)
    blog = models.URLField(max_length=30, null=True)

    # nickname = models.CharField(help_text="닉네임", max_length=40, blank=True)
    # image = models.ImageField(help_text="대표 이미지",blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Profiles"