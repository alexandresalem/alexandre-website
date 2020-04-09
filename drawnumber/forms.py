from django import forms
from .models import *


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['drawing','drawingcode']

