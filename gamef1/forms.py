from django import forms
from .models import Formula


# Create your form
class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['image']
