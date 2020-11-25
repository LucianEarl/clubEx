from django.db.models import query
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from djstripe.models import Product
from django.views.generic import ListView
from .forms import AccountForm, RatingForm, UploadForm
from .functions import handle_uploaded_file
from .models import Category, Exercise, UserVidWatch
import logging

logger = logging.getLogger(__name__)

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
    category_exercise = Exercise.objects.all().order_by('-views')
    featured = category_exercise[0]
    categories = Category.objects.all().order_by('category_name')
    return render(request, 'exercise.html', {'category_exercise':category_exercise, 'categories':categories, 'featured':featured})

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

@login_required
def videoDetail(request, pk):
    form = RatingForm(request.POST)
    if form.is_valid():
        video=Exercise.objects.get(pk=pk)
        star = form.cleaned_data.get('stars')
        video.stars = int(star)*20
        video.save()
    else:
        form = RatingForm()
    object = Exercise.objects.get(pk=pk)
    object.views = object.views+1
    object.save()

    if UserVidWatch.objects.filter(joined_video = object.pk, joined_user = request.user.id).exists():
        currentUserVid = UserVidWatch.objects.get(joined_user=request.user.id, joined_video=object.pk)
        currentUserVid.specific_views = currentUserVid.specific_views + 1
        currentUserVid.save()
        logger.error("increased user views")
    else:
        UserVidWatch.objects.create(joined_video=object.pk, joined_user=request.user.id, specific_views = 1)
        currentUserVid = UserVidWatch.objects.get(joined_user=request.user.id, joined_video=object.pk)
        logger.error("made a new row")

    return render(request, 'video.html', {'pk':pk, 'object':object,'currentUserVid':currentUserVid, 'form':form})

class SearchResultsView(ListView):
    model = Exercise
    template_name= 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Exercise.objects.filter(exercise_name__icontains=query)
