from django.db import models
from django.db.models.fields import DateField, DateTimeField, IntegerField, TextField, TimeField
from django.db.models.fields.related import ForeignKey

from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model

class YMD(models.Model):
    full_date = DateField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.full_date}"

class Year(models.Model):
    o_year = IntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.o_year}"

class Month(models.Model):
    o_month = IntegerField(blank=True, null=True)
    f_year = models.ForeignKey(Year, on_delete=models.SET_NULL, blank=True, null=True, related_name='month')
    def __str__(self) -> str:
        return f"{self.o_month}"

class Day(models.Model):
    o_day = IntegerField()
    f_month = models.ForeignKey(Month, on_delete=models.SET_NULL, blank=True, null=True, related_name='day')
    f_ymd = models.ForeignKey(YMD, on_delete=models.SET_NULL, blank=True, null=True, related_name='day')
    def __str__(self) -> str:
        return f"{self.o_day}"

class Event(models.Model):
    o_event_title = models.CharField(max_length=100, blank=True, null=True)
    o_event_time = models.CharField(max_length=100, blank=True, null=True)
    remain = IntegerField(blank=True, null=True)
    f_ymd = models.ForeignKey(YMD, on_delete=models.SET_NULL, blank=True, null=True, related_name='event')
    create_time = DateTimeField(auto_now=True, blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.o_event_title}"

class Time(models.Model):
    # o_time = TimeField(blank=True, null=True)
    f_event = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=True, null=True, related_name='time')
    f_ymd = models.ForeignKey(YMD, on_delete=models.SET_NULL, blank=True, null=True, related_name='time')
    f_person = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='time')
    create_time = DateTimeField(auto_now=True, blank=True, null=True)