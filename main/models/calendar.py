from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

class Year(models.Model):
    year = models.IntegerField(blank=False, null=False)

class Day(models.Model):
    day = models.IntegerField(blank=False, null=False)
    link_year = models.ForeignKey(Year, on_delete=models.CASCADE)