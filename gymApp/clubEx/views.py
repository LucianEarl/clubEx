from django.shortcuts import render
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
    products = Product.objects.all()
    return render(request, "subscription.html",{"products": products})


def complete(request):
	return render(request, "complete.html")
