from django import forms
from .models import Formula

#
# def test():
#     result = 'Xam2'
#     return result


# Create your form
class FormulaForm(forms.ModelForm):
    # def save(self, commit=True):
    #     m = super(FormulaForm, self).save(commit=False)
    #     # do custom stuff
    #     self.imagephoto = test()
    #     if commit:
    #         m.save()
    #     return m

    class Meta:
        model = Formula
        fields = ['imagelink']

        help_texts = {
            'imagelink': 'Group to which this message belongs to',
        }
