from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from rate.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('rate/',include("rate.urls")),
    url(r'accounts/profile/',UserProfile,name='user_profile'),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', UserCreateView.as_view(), name="signup")
]


