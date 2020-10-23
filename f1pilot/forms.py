from django import forms


class F1PilotForm(forms.Form):
    id_game = forms.IntegerField(required=None)
