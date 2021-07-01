from django.urls import path
from calendarapp import views

app_name = 'calendarapp'

urlpatterns = [
    path('', views.calendar, name='calendar_main'),
]