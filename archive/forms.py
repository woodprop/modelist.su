from django import forms
from .models import PlanImage


class PlanImageForm(forms.ModelForm):
    class Meta:
        model = PlanImage
        fields = ['image', 'subject']
