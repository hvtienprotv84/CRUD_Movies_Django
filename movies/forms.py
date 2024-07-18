from django import forms
from .models import *
from django.forms import ModelForm

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','year','desc','image']