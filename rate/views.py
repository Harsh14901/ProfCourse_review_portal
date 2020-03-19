from django.shortcuts import render
from django.http import HttpResponse
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


class ProfDetailView(DetailView):
    model=Profs
    
    # def get_queryset(self):
    #     q1 = super().get_queryset()
    #     print(q1)
        
    #     return q1.filter(pk=int(self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
    
    
    template_name = "prof/prof_page.html"
    context_object_name = "prof_data"


class CourseDetailView(DetailView):
    model=Courses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    template_name = "course/course_page.html"
    context_object_name = "course_data"

# def ProfPage(request,prof_id):
#     return render(request=request,template_name="prof/prof_page.html",context={"prof_data":Profs.objects.get(id=prof_id)})
    
# def CoursePage(request,course_id):
#     print("Course Page called")
#     return render(request=request,template_name="course/course_page.html",context={"course_data":Courses.objects.get(id=course_id)})
    
