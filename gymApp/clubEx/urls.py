from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path
from gymApp import settings
from .views import home, subscriptions, complete

urlpatterns = [
    path('', home, name='home'),
    path('subscribe/', subscriptions, name="subscription"),
	path("complete/", complete, name="complete"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
