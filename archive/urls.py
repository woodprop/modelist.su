from django.urls import path
from .views import *

urlpatterns = [
    # path('', hello),
    path('plans/', PlansList.as_view(), name='plans_list_url'),
    path('plans/upload/', PlanUpload.as_view(), name='plan_upload_url'),
    path('plans/<slug>/', PlanDetail.as_view(), name='plan_detail_url'),
]