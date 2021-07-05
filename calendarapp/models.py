from django.db import models
from django.db.models.fields import DateField, DateTimeField, IntegerField, TimeField
from django.db.models.fields.related import ForeignKey

from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model

class YMD(models.Model):
    full_date = DateField(blank=True, null=True)

class Year(models.Model):
    o_year = IntegerField(blank=True, null=True)
    
class Month(models.Model):
    o_month = IntegerField(blank=True, null=True)
    f_year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True, null=True)

class Day(models.Model):
    o_day = IntegerField()
    f_month = models.ForeignKey(Month, on_delete=models.CASCADE, blank=True, null=True)
    f_ymd = models.ForeignKey(YMD, on_delete=models.CASCADE, blank=True, null=True)
    remain = IntegerField(blank=True, null=True)

class Time(models.Model):
    o_time = TimeField(blank=True, null=True)
    f_ymd = models.ForeignKey(YMD, on_delete=models.CASCADE, blank=True, null=True)
    f_person = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    create_time = DateTimeField(auto_now=True, blank=True, null=True)
