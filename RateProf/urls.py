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
    url(r'accounts/profile/$',UserProfile,name='user_profile'),
    url(r'accounts/profile/clear/$',ClearUserWarnings,name='clear_warnings'),
    url(r'accounts/login/', auth_views.LoginView.as_view(authentication_form=AuthenticationFormCheckBanned), name='user_login'),
    url(r'accounts/logout', LogoutLog.as_view(),name="logout"),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('accounts/', include('django.contrib.auth.urls')),
    
    
    url(r'^signup/$', UserCreateView.as_view(), name="signup"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'accounts/', include('allauth.urls')),
]


