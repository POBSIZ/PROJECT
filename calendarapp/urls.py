from django.urls import path
from calendarapp.views import * 

app_name = 'calendarapp'

urlpatterns = [
    path('', ShowCalendar, name='calendar_main'),
    path('view/', ReservationView, name='calendar_view'),
    path('resv/', Reserve, name='calendar_resv'),
    path('cancel/', CancelReservation, name='calendar_cancel'),
]