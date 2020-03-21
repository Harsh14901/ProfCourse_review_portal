from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('rate/',include("rate.urls")),
    url('accounts/', include('django.contrib.auth.urls'))
]
