from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect

#home view
def home(request):
    return render(request, "home.html")