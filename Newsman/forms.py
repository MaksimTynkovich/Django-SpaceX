from multiprocessing.sharedctypes import Value
from django import forms
from matplotlib import widgets
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        # prepopulated_fields = {"slug": ("title",)}

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

    def clean_category(self):
        category = self.cleaned_data['category']
        if category is None:
            raise ValidationError('Категория не выбрана')
        return category

    # def save(self, *args): 
    #     self.slug = slugify(self.title)
    #     super().save(*args)