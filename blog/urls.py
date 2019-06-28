from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<slug>/edit/', PostEdit.as_view(), name='post_edit_url'),
    path('post/<slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<slug>/edit/', TagEdit.as_view(), name='tag_edit_url'),
    path('tag/<slug>/delete/', TagDelete.as_view(), name='tag_delete_url',)

]
