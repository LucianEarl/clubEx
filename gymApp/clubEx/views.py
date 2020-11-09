from django.shortcuts import render
from djstripe.models import Product
from django.contrib.auth.decorators import login_required

#home view
def home(request):
    return render(request, "home.html")

#subscriptions
@login_required
def subscriptions(request):
    products = Product.objects.all()
    return render(request, "subscription.html",{"products": products})


def complete(request):
	return render(request, "complete.html")