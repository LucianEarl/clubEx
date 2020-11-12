from django.http.response import HttpResponseRedirect
from .forms import AccountForm
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
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['addSub']
            name = request.user
            name.subscription_plan = f
            name.save()
            return HttpResponseRedirect('/complete/')
    else:
        form = AccountForm()

    return render(request, "subscription.html",{"products": products, 'form':form})


def complete(request):
	return render(request, "complete.html")

def videos(request):
	return render(request, "videos.html")
