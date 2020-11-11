from django.db import models
from django.db.models import fields
from django.forms import forms
from django.forms.models import ModelForm
from account.models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ('subscription_plan',)
        