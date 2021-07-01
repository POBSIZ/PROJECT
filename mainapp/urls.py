from django.urls import path

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.base, name='main'),
    path('notice/', views.notice, name='notice'),
    path('error/', views.error, name='error'),
]