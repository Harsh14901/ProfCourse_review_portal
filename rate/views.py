from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from rate.models import *

import random
import names
# Create your views here.

class ProfsListView(ListView):
    model = Dept
    template_name = "prof/profs.html"
    context_object_name = "dept_list"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        """ Populating the Profs and Courses table """

        # dl = Dept.objects.all()
        # for dept in dl:
        #     for i in range(5):
        #         uname = names.get_first_name()
        #         name = uname + " " + names.get_last_name()
        #         uname = uname.lower()
        #         email = f"{uname}@{dept.name.lower()}.iitd.ac.in"
        #         webpage = f"web.iitd.ac.in/~{uname}"
        #         print(uname,name,webpage,email)

        #         p1 = Profs(dept=dept,name=name,email=email,webpage=webpage)
        #         p1.save()

        #         code = dept.name.upper() + str(random.randint(100,800))
        #         title = f"Course Title for {code}"

        #         c1 = Courses(dept=dept,title=title,code=code)
        #         c1.save()
        #         print(code,title)

        """ Populating Reviews for profs and courses """

        # dl = Dept.objects.all()
        # for dept in dl:
        #     pl = Profs.objects.filter(dept=dept)
        #     cl = Courses.objects.filter(dept=dept)
        #     for i in range(4):
        #         r = Review()
        #         r.prof = pl[random.randint(0,len(pl)-1)]
        #         r.course = cl[random.randint(0,len(cl)-1)]
        #         r.difficulty = random.randint(0,5)
        #         r.content_quality = random.randint(0,5)
        #         r.grading = random.randint(0,5)
        #         r.attendance = random.randint(0,5)
        #         r.overall_rating = random.randint(0,5)

        #         r.actual_name = names.get_full_name()
        #         r.username = r.actual_name.split()[0].lower()
        #         r.email = f"{r.username}{str(random.randint(0,1000))}@gmail.com"
        #         r.isAnonymous = bool(random.randint(0,1))

        #         r.comment = f"This is a sample comment to test out during development"
                
        #         print(r.prof,r.course,r.username,r.actual_name,r.comment,r.email)
        #         r.save()

        return context
    

class CoursesListView(ListView):
    model = Dept
    template_name = "course/courses.html"
    context_object_name = "dept_list"


class ProfDetailView(DetailView):
    model=Profs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['prof_data'].review_set.all()
        # print(context['reviews'])
        return context
    
    template_name = "prof/prof_page.html"
    context_object_name = "prof_data"


class CourseDetailView(DetailView):
    model=Courses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['course_data'].review_set.all()
        return context
    

    template_name = "course/course_page.html"
    context_object_name = "course_data"

# def ProfPage(request,prof_id):
#     return render(request=request,template_name="prof/prof_page.html",context={"prof_data":Profs.objects.get(id=prof_id)})
    
# def CoursePage(request,course_id):
#     print("Course Page called")
#     return render(request=request,template_name="course/course_page.html",context={"course_data":Courses.objects.get(id=course_id)})
    
