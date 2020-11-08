from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect

#home view
def home(request):
    return render(request, "home.html")

#subscriptions
def subscriptions(request):
    return render(request, "subscription.html")

#login view
def login(request):
    return render(request, "login.html")
