from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from rate.models import *
# Create your views here.

class ProfsListView(ListView):
    model = Dept
    template_name = "prof/profs.html"
    context_object_name = "dept_list"

class CoursesListView(ListView):
    model = Dept
    template_name = "course/courses.html"
    context_object_name = "dept_list"




    