from django.urls import path
from calendarapp import views

app_name = 'calendarapp'

urlpatterns = [
    path('', views.calendar, name='calendar_main'),
    path('view/', views.view, name='calendar_view'),
    path('resv/', views.resv, name='calendar_resv'),
    path('cancel/', views.resvCancel, name='calendar_cancel'),
]