from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView
from gymApp import settings
from .views import home

urlpatterns = [
    path('', home, name='home'),


]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]


urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)