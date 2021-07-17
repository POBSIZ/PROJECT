from django.db import models
from django.db.models import fields
from rest_framework import serializers
from calendarapp.models import Time, YMD
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username')


class YMDSerializer(serializers.ModelSerializer):
    class Meta:
        model = YMD
        fields = ('full_date')

        
class TimeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='f_person.username')

    class Meta:
        model = Time
        fields = ('o_time', 'username', 'create_time')