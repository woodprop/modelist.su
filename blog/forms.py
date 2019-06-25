from django import forms
from .models import Tag

from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug должен быть уникальным. Slug "{}" уже существует'.format(new_slug))
        if new_slug == 'create':
            raise ValidationError('Slug не может быть "Create"')
        return new_slug



