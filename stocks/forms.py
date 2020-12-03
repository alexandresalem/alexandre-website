from django import forms
from django_select2.forms import Select2Widget, ModelSelect2Widget, ModelSelect2MultipleWidget
from .models import Company
from django_select2 import forms as s2forms


class CompanyForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=ModelSelect2Widget(
            queryset=Company.objects.all(),
            model=Company,
            search_fields=['name__icontains', 'symbol__icontains'],
            attrs={'style': 'width:60%'}
        ),
        required=True,
        label="Company",
        # help_text="Search for a company's name or symbol"
    )
