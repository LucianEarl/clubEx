from .functions import handle_uploaded_file
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import AccountForm, UploadForm
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from djstripe.models import Product
from django.contrib.auth.decorators import login_required
from .models import Category, Exercise

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
            name.is_subscribed = True
            name.save()
            return HttpResponseRedirect('/complete/')
    else:
        form = AccountForm()

    return render(request, "subscription.html",{"products": products, 'form':form})

@login_required
def category(request, pk):
    ca_exercise = Exercise.objects.filter(category=pk)
    
    categories = Category.objects.all()
    return render(request, 'categories.html', {'pk':pk,'ca_exercise':ca_exercise, 'categories':categories})


def exercises(request):
    category_exercise = Exercise.objects.all()
    categories = Category.objects.all()
    return render(request, 'exercise.html', {'category_exercise':category_exercise, 'categories':categories})

def complete(request):
	return render(request, "complete.html")

def videos(request):
	return render(request, "video.html")

def upload(request):  
    if request.method == 'POST':  
        form=UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        handle_uploaded_file(request.FILES['videofile'])  
        return HttpResponseRedirect('/exercises/')  
    else:  
        video = UploadForm()  
        return render(request,"upload.html",{'form':video})  


# class VideoView(generic.ListView):
#     model = Exercise
#     template_name = 'videos.html'

# def exercise(request, pk):
#     try:
#         exercise = Exercise.objects.get(id = pk)
#     except Exercise.DoesNotExist:
#         raise Http404('exercise not found')

#     return render(request, 'exercise.html', {'exercise': exercise})
