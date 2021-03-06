import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.views import View
from .models import *
from .forms import *


def get_file_size(file):
    byte_size = os.path.getsize('media/' + str(file))
    mb_size = round(byte_size / 1024 / 1024, 2)
    return mb_size


class PlansList(View):
    def get(self, request):
        plans = Plan.objects.all()
        paginator = Paginator(plans, 1)
        page = paginator.get_page(request.GET.get('page', 1))
        return render(request, 'archive/plans_list.html', context={'plans': page})


class PlanDetail(View):
    def get(self, request, slug):
        plan = Plan.objects.get(slug__iexact=slug)
        plan.file_size = str(get_file_size(plan.file)) + ' MB'
        return render(request, 'archive/plan_detail.html', context={'plan': plan})


class PlanUpload(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        form = PlanForm
        return render(request, 'archive/plan_upload_form.html', context={'form': form})

    def post(self, request):
        bound_form = PlanForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_plan = bound_form.save()
            return redirect(new_plan)
        return render(request, 'archive/plan_upload_form.html', context={'form': bound_form})


class TagDetail(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'archive/tag_detail.html', context={'tag': tag})



