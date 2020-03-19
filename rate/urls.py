from django.urls import path
from django.conf.urls import url
from rate.views import *

urlpatterns = [
    url(r'^profs/',ProfsListView.as_view(),name="profs"),
    url(r'^courses/',CoursesListView.as_view(),name="courses"),
]
