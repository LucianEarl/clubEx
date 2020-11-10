# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.urls import include, path
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', include('clubEx.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



