from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
#home view
def home(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'home.html', context)

#subscriptions
def subscriptions(request):
    return render(request, "subscription.html")
