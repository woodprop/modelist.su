from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>', post_detail, name='post_detail_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/<slug>', tag_detail, name='tag_detail_url'),
]
