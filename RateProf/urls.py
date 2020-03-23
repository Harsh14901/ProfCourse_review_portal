from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from rate.views import *
import django.contrib.auth.views as auth_views
from rate.forms import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('rate/',include("rate.urls")),
    url(r'accounts/profile/',UserProfile,name='user_profile'),
    url(r'accounts/login/', auth_views.LoginView.as_view(authentication_form=AuthenticationFormCheckBanned), name='user_login'),
    url(r'accounts/logout', LogoutLog.as_view(),name="logout"),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', UserCreateView.as_view(), name="signup")
]


