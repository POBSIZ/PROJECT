from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'main.html')

def notice(request):
    return render(request, 'notice.html')

def error(request):
    return render(request, 'error.html')

