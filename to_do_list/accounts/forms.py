from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import Account


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Add a email address")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError("This email already in use")

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError("This username already in use")


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control mb-1",
                                                              "type": "email",
                                                              "name": "email", }), max_length=255, label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "type": "password",
                                                                 "name": "password", }))
