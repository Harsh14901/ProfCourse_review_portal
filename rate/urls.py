from django.urls import path
from django.conf.urls import url
from rate.views import *
# import rate

urlpatterns = [
    url('^index/$', index, name="index"),

    url(r'^like/(?P<pk>[0-9]+)$',LikeReview,name="like"),
    url(r'^dislike/(?P<pk>[0-9]+)$',DislikeReview,name="dislike"),
    
    url(r'^report/(?P<pk>[0-9]+)/$',ReportCreateView.as_view() , name="report"),
    # url(r'^profs/(?P<prof_id>[0-9]+)/$', ProfPage, name="p_data"),
    url(r'^profs/(?P<pk>[0-9]+)/$', ProfPage, name="p_data"),
    url(r'^profs/(?P<pk>[0-9]+)/create/$',ProfReviewCreateView.as_view(), name="prof_review"),
    url(r'^profs/',ProfsListView.as_view(),name="profs"),
    
    # url(r'^courses/(?P<course_id>[0-9]+)/$',CoursePage,name="c_data"),
    url(r'^courses/(?P<pk>[0-9]+)/$',CoursePage,name="c_data"),
    url(r'^courses/(?P<pk>[0-9]+)/create/$',CourseReviewCreateView.as_view(), name="course_review"),
    url(r'^courses/', CoursesListView.as_view(), name="courses"),
]
