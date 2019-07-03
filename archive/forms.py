from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'author', 'image', 'file']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'author': 'Автор',
            'image': 'Изображение',
            'file': 'Архив с чертежом',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
