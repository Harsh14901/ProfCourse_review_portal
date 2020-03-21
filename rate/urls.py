from django.urls import path
from django.conf.urls import url
from rate.views import *
# import rate

urlpatterns = [
    
    # url(r'^profs/(?P<prof_id>[0-9]+)/$', ProfPage, name="p_data"),
    url(r'^profs/(?P<pk>[0-9]+)/$', ProfPage, name="p_data"),
    url(r'^profs/(?P<pk>[0-9]+)/create/$',ProfReviewCreateView.as_view(), name="prof_review"),
    url(r'^profs/',ProfsListView.as_view(),name="profs"),
    
    # url(r'^courses/(?P<course_id>[0-9]+)/$',CoursePage,name="c_data"),
    url(r'^courses/(?P<pk>[0-9]+)/$',CoursePage,name="c_data"),
    url(r'^courses/(?P<pk>[0-9]+)/create/$',CourseReviewCreateView.as_view(), name="course_review"),
    url(r'^courses/', CoursesListView.as_view(), name="courses"),
]
