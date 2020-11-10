from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.shortcuts import render
from djstripe.models import Product
from django.contrib.auth.decorators import login_required

#home view
def home(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'home.html', context)

#subscriptions
@login_required
def subscriptions(request):
    return render(request, "subscription.html")
    products = Product.objects.all()
    return render(request, "subscription.html",{"products": products})


def complete(request):
	return render(request, "complete.html")
