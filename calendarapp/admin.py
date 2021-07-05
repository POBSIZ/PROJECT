from django.contrib import admin

from .models import YMD, Year, Month, Day, Time

admin.site.register(YMD)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Time)