from django import forms
from .models import Formula


# Create your form
class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['imagelink']

        help_texts = {
            'imagelink': 'Group to which this message belongs to',
        }
