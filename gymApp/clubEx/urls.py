from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path
from gymApp import settings
from .views import home, subscriptions, complete, upload, videos, category, exercises
from django.contrib import admin
from account.views import(
    signup_view, user_detail,
)

urlpatterns = [
    path('', home, name='home'),
    path('subscribe/', subscriptions, name="subscription"),
    path('signup/', signup_view, name='signup'),
    path('user_detail/', user_detail, name='user_detail'),
    path('video/', videos, name='video'),
    path('upload/', upload, name='upload'),
    path('exercises/', exercises, name='exercises'),
    path('category/<int:pk>/', category, name='category')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path("complete/", complete, name="complete"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
