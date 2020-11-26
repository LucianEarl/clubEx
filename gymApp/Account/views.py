from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import SignUpForm
from .models import Account

def signup_view(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['signup_form'] = form
    else:
        form = SignUpForm()
        context['signup_form'] = form
    return render(request, 'account/signup.html', context)


def user_detail(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'account/user_detail.html', context)

"""
---------------------------------------------------------------------------------------------------------------------------------------------
signup_view is an object that is being defined to call a request function
to respond to an object with all it's data, especially content.
the user_detail is an object that is also calling a request function to
respond.

user_detail is an object that is being defined to call a request function
to respond to all other objects in Account.
---------------------------------------------------------------------------------------------------------------------------------------------
"""