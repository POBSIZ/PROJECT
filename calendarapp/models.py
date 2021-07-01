from django.db import models
from django.db.models.fields import DateField, IntegerField
from django.db.models.fields.related import ForeignKey

class YMD(models.Model):
    full_date = DateField

class Year(models.Model):
    year = IntegerField()

class Month(models.Model):
    month = IntegerField()
    o_year = models.ForeignKey(Year)

class Day(models.Model):
    day = IntegerField()
    o_month = models.ForeignKey(Month)
    o_ymd = models.ForeignKey(YMD, blank=True, null=True)

