from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.core import serializers
from .models import YMD, Year, Month, Day, Time

# CALENDAR
@login_required(login_url='accountapp:login')
def ShowCalendar(request):
    return render(request, 'calendar/calendar.html')

# VIEW
@login_required(login_url='accountapp:login')
def ReservationView(request):
    if (request.method == 'POST'):

        # YMD
        try:
            YMD.objects.get(full_date=request.POST['a_ymd'])
        except:
            ymd_obj = YMD()
            ymd_obj.full_date = request.POST['a_ymd']
            ymd_obj.save()

        # Year
        try:
            Year.objects.get(o_year=request.POST['a_year'])
        except:
            year_obj = Year()
            year_obj.o_year = request.POST['a_year']
            year_obj.save()

        # Month
        try:
            Month.objects.get(o_month=request.POST['a_month'])
        except:
            f_year_obj = Year.objects.get(o_year=request.POST['a_year'])
            month_obj = Month()
            month_obj.o_month = request.POST['a_month']
            month_obj.f_year = f_year_obj   
            month_obj.save()

        # Day
        try:
            f_ymd_obj = YMD.objects.get(full_date=request.POST['a_ymd'])
            r_day = Day.objects.get( f_ymd=f_ymd_obj )
            res_remain = r_day.remain
        except:
            f_ymd_obj = YMD.objects.get(full_date=request.POST['a_ymd'])
            f_month_obj = Month.objects.get(o_month=request.POST['a_month'])
            day_obj = Day()
            day_obj.o_day = request.POST['a_day']
            day_obj.remain = 4
            day_obj.f_month = f_month_obj
            day_obj.f_ymd = f_ymd_obj
            day_obj.save()
            res_remain = 4

        # Time
        try: 
            f_ymd_obj = YMD.objects.get(full_date=request.POST['a_ymd'])
            time_obj = Time.objects.filter(f_ymd=f_ymd_obj)
            time_obj = serializers.serialize("json", time_obj)
            # print(time_obj)
        except:
            time_obj = False


    else:
        return render(request, 'error.html')
    context = {  
        'remain': res_remain,    
        'time': time_obj,    
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
    # return HttpResponse(context)

# RESV
@login_required(login_url='accountapp:login')
def Reserve(request):
    if (request.method == 'POST'):
        f_ymd_obj = YMD.objects.get(full_date=request.POST['a_ymd'])
        try:
            r_day = Day.objects.get(f_ymd=f_ymd_obj)
            if(r_day.remain == 0):
                res_remain = True
            else:
                r_time = Time.objects.get( Q(f_ymd=f_ymd_obj) & Q(f_person=request.user) )
                res_remain = False
        except:
            time_obj = Time()
            time_obj.o_time = request.POST['a_time']
            time_obj.f_ymd = f_ymd_obj
            time_obj.f_person = request.user
            time_obj.save()
            
            r_day = Day.objects.get(f_ymd=f_ymd_obj)
            if(r_day.remain == 0):
                res_remain = True
            else:
                r_day.remain = r_day.remain - 1
                r_day.save()
                res_remain = r_day.remain

    context = {  
        'remain': res_remain,    
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required(login_url='accountapp:login')
def CancelReservation(request):
    if (request.method == 'POST'):
        f_ymd_obj = YMD.objects.get(full_date=request.POST['a_ymd'])
        try:
            r_time = Time.objects.get( Q(f_ymd=f_ymd_obj) & Q(f_person=request.user) )
            r_time.delete()

            r_day = Day.objects.get(f_ymd=f_ymd_obj)
            r_day.remain = r_day.remain + 1
            r_day.save()
            res_remain = r_day.remain 
        except:
            res_remain = False
    context = {  
        'remain': res_remain,    
    }
    return HttpResponse(json.dumps(context), content_type="application/json")