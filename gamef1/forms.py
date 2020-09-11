from django import forms
from .models import F1Prediction


class F1PredictionResultForm(forms.ModelForm):

    class Meta:
        model = F1Prediction
        fields = ['season', 'constructor', 'chassis']
        widgets = {
            'constructor': forms.HiddenInput(),
            'season': forms.HiddenInput(),
            'chassis': forms.HiddenInput()
        }
