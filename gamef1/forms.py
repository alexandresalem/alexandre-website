from django import forms
from .models import Formula

#
# def test():
#     result = 'Xam2'
#     return result


# Create your form
class FormulaForm(forms.ModelForm):

    imagephoto = forms.CharField(required=False)

    class Meta:
        model = Formula
        fields = ['imagelink','imagephoto']

        help_texts = {
            'imagelink': 'Group to which this message belongs to',
        }
