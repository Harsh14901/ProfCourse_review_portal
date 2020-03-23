from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from rate.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
import random
import names
from datetime import datetime as dt
from django.contrib.auth.views import LoginView,LogoutView
from django.core.exceptions import ValidationError
# Create your views here.


def index(request):
    """ Adding users to the database and giving user info to all reviews """

    """ Adding 10 users """
    # for i in range(10):
    #     f_name = names.get_first_name()
    #     l_name = names.get_last_name()
    #     email = f"{f_name}{random.randint(1000,9000)}@gmail.com"
    #     user = User(username=f"user{i+1}",password=f"user{i+1}@123",first_name=f_name,last_name=l_name,email=email)
    #     print(user.email)
    #     user.save()
    
    # for review in Review.objects.all():
    #     ul = User.objects.exclude(username="admin")
    #     user = ul[random.randint(0,len(ul)-1)]
    #     stamp = dt(random.randint(2016,2019),random.randint(1,12),random.randint(1,28),random.randint(0,13),random.randint(0,59),random.randint(0,59))
    #     review.timestamp = stamp
    #     review.user = user
    #     print(review.timestamp,review.user)
    #     review.save()
        
    
    return render(request,template_name="index.html")

class ProfsListView(ListView):
    model = Dept
    template_name = "prof/profs.html"
    context_object_name = "dept_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # print(self.request.session)
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


# class ProfDetailView(DetailView):
#     model=Profs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = context['prof_data'].review_set.all()
#         # print(context['reviews'])
#         return context

#     template_name = "prof/prof_page.html"
#     context_object_name = "prof_data"


# class CourseDetailView(DetailView):
#     model=Courses

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = context['course_data'].review_set.all()
#         return context


#     template_name = "course/course_page.html"
#     context_object_name = "course_data"

def ProfPage(request, pk):
    prof_data = get_object_or_404(Profs,pk=pk)
    return render(request=request, template_name="prof/prof_page.html", context={"prof_data": prof_data, "reviews": prof_data.review_set.all(),"id":pk})


def CoursePage(request, pk):
    course_data = get_object_or_404(Courses, pk=pk)
    return render(request=request, template_name="course/course_page.html", context={"course_data": course_data, "reviews": course_data.review_set.all(),"id":pk})


# @login_required(login_url="/accounts/login/")
# def AddReview(request):
#     return HttpResponse("You have been authenticated")

class ProfReviewCreateView(LoginRequiredMixin,CreateView):
    login_url = "/accounts/login"
    template_name = "form/review_form.html"
    form_class = ReviewForm
    # labels = {'content_quality':"how good was the content",'isAnonymous' : "Remain anonymous?"}
    def get_success_url(self):
        print(self.kwargs['pk'])
        # print(reverse("p_data",args=self.kwargs['pk']))
        return reverse("p_data",args=[self.kwargs['pk']])
        # return f"/rate/profs/{str(self.kwargs['pk'])}/"
    def form_valid(self, form):
        form.instance.user = self.request.user
        comment_activity = Activity(user=self.request.user,category=Activity.COMMENT)
        comment_activity.comment_log(form.save())
        comment_activity.save()
        return super().form_valid(form)
    
    
    def get_initial(self):
            prof = get_object_or_404(Profs, id=self.kwargs['pk'])
            return {"prof": prof} 

            
class CourseReviewCreateView(LoginRequiredMixin,CreateView):
    login_url = "/accounts/login"
    template_name = "form/review_form.html"
    form_class = ReviewForm
    # labels = {'content_quality':"how good was the content",'isAnonymous' : "Remain anonymous?"}
    def get_success_url(self):
            return reverse("c_data", args=self.kwargs['pk'])
    def form_valid(self, form):
        form.instance.user = self.request.user
        comment_activity = Activity(user=self.request.user, category=Activity.COMMENT)
        comment_activity.comment_log(form.save())
        comment_activity.save()
        return super().form_valid(form)
    
    
    def get_initial(self):
            course = get_object_or_404(Courses, id=self.kwargs['pk'])
            return {"course": course}


class UserCreateView(CreateView):
    model = User
    template_name = "form/signup.html"
    form_class = SignUpForm
    success_url = "/accounts/profile/"

@login_required(login_url="/accounts/login/")
def UserProfile(request):
    activity = request.user.review_set.all().order_by("-timestamp")
    return render(request,template_name="profile.html",context={"reviews":activity})


class ReportCreateView(LoginRequiredMixin,CreateView):
    login_url = "/accounts/login/"
    model = ReportReview
    template_name = "form/report_form.html"
    fields = ['category','reason']
    success_url = "/accounts/profile"

    def form_valid(self, form):
        review = get_object_or_404(Review,id=self.kwargs['pk'])
        form.instance.review = review
        form.instance.reporting_user = self.request.user
        
        report_activity = Activity(user=self.request.user,category=Activity.REPORT)
        report_activity.report_log(report=form.save())
        report_activity.save()

        return super().form_valid(form)

    
class LogoutLog(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout_activity = Activity(user=self.request.user,category=Activity.LOGOUT)
        logout_activity.logout_log()
        logout_activity.save()
        return super().dispatch(request, *args, **kwargs)
    