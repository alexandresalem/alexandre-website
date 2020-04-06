from django import forms
import datetime
#
BIRTH_YEAR_CHOICES = ['2017','2018','2019','2020']
GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ]

WEIGHT = [
    ('pounds','Pounds'),
    ('kilos','Kilos')
]

HEIGHT = [
    ('meters','Centimeters'),
    ('inches','Inches')
]
class BabyForm(forms.Form):

    dob = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    dom = forms.DateField(label='Date of Measurement', widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),initial=datetime.date.today())
    gender = forms.ChoiceField(choices=GENDER)

    weight_format = forms.ChoiceField(choices=WEIGHT, label="Weight's Format")
    weight=forms.IntegerField(label='Weight', initial="Baby's Weight")

    height_format = forms.ChoiceField(choices=HEIGHT)
    height = forms.IntegerField(label='Height', error_messages={'required':'Please enter your height'})

