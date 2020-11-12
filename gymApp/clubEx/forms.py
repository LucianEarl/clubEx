from django.db import models
from django.db.models import fields
from django import forms
from django.forms.models import ModelForm
from account.models import Account

class AccountForm(forms.Form):
    addSub = forms.CharField(max_length=100)
   
        