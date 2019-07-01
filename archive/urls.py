from django.urls import path
from .views import *

urlpatterns = [
    path('', hello),
    path('plans/', PlansList.as_view(), name='plans_list_url'),
    path('plan/<slug>/', PlanDetail.as_view(), name='plan_detail_url'),
    path('image/upload/', ImageUpload.as_view(), name='image_upload_url'),
]