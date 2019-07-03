from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.views import View
from .models import *
from .forms import *
from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>Hello from archive</h1>')


class PlansList(View):
    def get(self, request):
        plans = Plan.objects.all()
        return render(request, 'archive/plans_list.html', context={'plans': plans})


class PlanDetail(View):
    def get(self, request, slug):
        plan = Plan.objects.get(slug__iexact=slug)
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



