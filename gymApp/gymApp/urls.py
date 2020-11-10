# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.urls import include, path
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve


admin.autodiscover()

urlpatterns = [
    path('', include('clubEx.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



