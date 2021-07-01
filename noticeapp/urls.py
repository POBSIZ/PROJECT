from django.urls import path
from django.views.generic import TemplateView

from noticeapp.views import *

app_name = 'noticeapp'

urlpatterns = [
    path('list/', NoticeListView.as_view(), name="list"),
    path('create/', Notice_create, name="create"),
    path('detail/<int:pk>', NoticeDetailView.as_view(), name="detail"),
    path('update/<int:pk>', NoticeUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', NoticeDeleteView.as_view(), name="delete"),
]