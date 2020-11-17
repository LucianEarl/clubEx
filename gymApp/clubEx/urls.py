from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path
from gymApp import settings
from .views import home, subscriptions, complete, videos, category
from django.contrib import admin
from account.views import(
    signup_view, user_detail,
)

urlpatterns = [
    path('', home, name='home'),
    path('subscribe/', subscriptions, name="subscription"),
    # path('videos/', videos, name="videos"),
    # path('videos/', VideoView.as_view(), name="videos"),
    path('signup/', signup_view, name='signup'),
    path('user_detail/', user_detail, name='user_detail'),
    path('video/', videos, name='video'),
    path('category/<int:pk>/', category, name='category')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path("complete/", complete, name="complete"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
