from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Digite uma senha'}))

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'date_of_birth')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'Data de Nascimento'})
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password',
                  'date_of_birth',
                  'is_active',
                  'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Seu email'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha'}))
