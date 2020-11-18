from django.db.models import query
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from djstripe.models import Product
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .forms import AccountForm, UploadForm
from .functions import handle_uploaded_file
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
    ca_exercise = Exercise.objects.filter(category=pk).order_by('exercise_name')
    
    categories = Category.objects.all().order_by('category_name')
    return render(request, 'categories.html', {'pk':pk,'ca_exercise':ca_exercise, 'categories':categories})

@login_required
def exercises(request):
    category_exercise = Exercise.objects.all().order_by('exercise_name')
    categories = Category.objects.all().order_by('category_name')
    return render(request, 'exercise.html', {'category_exercise':category_exercise, 'categories':categories})

@login_required
def complete(request):
	return render(request, "complete.html")


@login_required
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

class VideoDetailView(DetailView):
    model = Exercise
    template_name = 'video.html'

    def VideoViews(self): # testing for video views

        if(Exercise.views.objects.count()<=0):
            x=Exercise.views.objects.create()
            x.save()
        else:
            x=Exercise.views.objects.all()[0]
            x.hits=x.hits+1
            x.save()
        context={'videoviews':x.hits}
        return render(self, 'video.html',context=context)
class SearchResultsView(ListView):
    model = Exercise
    template_name= 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Exercise.objects.filter(exercise_name__icontains=query)
def VideoViews(self):

    if(Exercise.views.objects.count()<=0):
        x=Exercise.views.objects.create()
        x.save()
    else:
        x=Exercise.views.objects.all()[0]
        x.hits=x.hits+1
        x.save()
    context={'videoviews':x.hits}
    return render(self, 'video.html',context=context)


# class VideoView(generic.ListView):
#     model = Exercise
#     template_name = 'videos.html'

# def exercise(request, pk):
#     try:
#         exercise = Exercise.objects.get(id = pk)
#     except Exercise.DoesNotExist:
#         raise Http404('exercise not found')

#     return render(request, 'exercise.html', {'exercise': exercise})
