from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

"""
---------------------------------------------------------------------------------------------------------------------------------------------
django.contrib is list of packages, .auth is an authentication framework.
Anything that comes after .auth is the content type such as models or
forms (example contrib.auth.forms) which is then imported elsewhere.
---------------------------------------------------------------------------------------------------------------------------------------------
"""

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Required. Please put in your username.')
    first_name = forms.CharField(max_length=30, help_text='Required. Please put in your first name.')
    last_name = forms.CharField(max_length=30, help_text='Required. Please put in your last name.')
    email = forms.EmailField(max_length=60, help_text='Required. Please put in your email.')
    physical_address = forms.CharField(max_length=300, help_text='Required. Please put in your home address.')
    phone_number = forms.CharField(max_length=10, help_text='Required. Please put in your phone number.')

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'physical_address', 'phone_number', 'password1', 'password2', )

"""
---------------------------------------------------------------------------------------------------------------------------------------------
The SignUpForm is an object that contains a list of characteristics within a
form such as username or email.
---------------------------------------------------------------------------------------------------------------------------------------------
"""