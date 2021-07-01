from django.shortcuts import render

# CALENDAR
def calendar(request):
    return render(request, 'calendar/calendar.html')