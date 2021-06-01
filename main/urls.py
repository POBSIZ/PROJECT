from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
    path('notice/', views.notice, name='notice'),
]
