from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'main.html')

def notice(request):
    return render(request, 'notice.html')

# CALENDAR
def calendar(request):
    return render(request, 'calendar/calendar.html')