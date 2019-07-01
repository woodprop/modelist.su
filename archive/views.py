from django.shortcuts import render
from django.views import View
from .models import Plan
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
        form = PlanForm
        return render(request, 'archive/plan_upload_form.html', context={'form': form})

    def post(self, request):
        bound_form = PlanForm(request.POST, request.FILES)

        if bound_form.is_valid():
            bound_form.save()
            return HttpResponse('<h1>OK</h1>')
        return render(request, 'archive/plan_upload_form.html', context={'form': bound_form})



