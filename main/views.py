from django.shortcuts import render

def index(request):
    return render(request, 'main.html')
    
def intro(request):
    return render(request, 'introduce.html')
    
def notice(request):
    return render(request, 'notice.html')



# CALENDAR
def calendar(request):
    return render(request, 'calendar/calendar.html')