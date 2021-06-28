from django.urls import path
from django.views.generic import TemplateView

from boardapp.views import *

app_name = 'boardapp'

urlpatterns = [
    path('list/', PostListView.as_view(), name="list"),
    path('create/', Post_create, name="create"),
    path('detail/<int:pk>', PostDetailView.as_view(), name="detail"),
    path('update/<int:pk>', PostUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', PostDeleteView.as_view(), name="delete"),
]