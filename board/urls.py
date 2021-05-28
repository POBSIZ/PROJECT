from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "board"

urlpatterns = [
    path('postlist/', views.Post_list, name='post_list'),
    path('detail/<int:post_id>/', views.Post_detail, name='post_detail'),
    path('post/create/', views.Post_create, name='post_create'),
    path('post/modify/<int:post_id>/', views.Post_modify, name='post_modify'),
    path('post/delete/<int:post_id>', views.Post_delete, name='post_delete'),
    
    path('comment/create/<int:post_id>/', views.Comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', views.Comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.Comment_delete, name='comment_delete'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)