from django import forms
from .models import Formula, Answer


# Create your form
class FormulaForm(forms.ModelForm):

    class Meta:
        model = Formula
        fields = ['f1image']


class AnswerForm(forms.ModelForm):
    GUESSES = (
        ('1st', "First"),
        ('2nd', 'Second'),
        ('3rd','Third')
    )
    guess = forms.CharField(widget=forms.RadioSelect(choices=GUESSES))
    class Meta:
        model = Answer
        fields = ['guess','chassis','team','link']