from django import forms
from .models import PlanImage, PlanFile


class PlanImageForm(forms.ModelForm):
    class Meta:
        model = PlanImage
        fields = ['image', 'subject']


class PlanFileForm(forms.ModelForm):
    class Meta:
        model = PlanFile
        fields = ['file', 'subject']
