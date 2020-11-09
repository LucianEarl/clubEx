from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path
from gymApp import settings
from .views import home, subscriptions
from django.contrib import admin
from account.views import(
    signup_view, user_detail,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('subscribe/', subscriptions, name="subscription"),
    path('signup/', signup_view, name='signup'),
    path('user_detail/', user_detail, name='user_detail'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
