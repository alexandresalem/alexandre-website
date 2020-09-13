from django import forms
from django_select2 import forms as s2forms
from .models import F1Prediction


class ChassisWidget(s2forms.ModelSelect2Widget):
    search_fields = ['constructor__icontains',
                     'chassis__icontains']


class F1PredictionResultForm(forms.ModelForm):

    class Meta:
        model = F1Prediction
        fields = ['season', 'constructor', 'chassis']
        widgets = {
            'constructor': forms.HiddenInput(),
            'season': forms.HiddenInput(),
            'chassis': forms.HiddenInput()
        }
