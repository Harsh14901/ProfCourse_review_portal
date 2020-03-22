from django.contrib.auth.forms import AuthenticationForm
from django import forms
from rate.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Email is Required")
    first_name = forms.CharField(max_length=50, required=False,help_text="Optional")
    last_name = forms.CharField(max_length=50, required=False, help_text="Optional")

    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['prof', 'course', 'difficulty', 'content_quality',
              'grading', 'attendance', 'overall_rating', 'isAnonymous', 'comment']
    
    def __init__(self,*args, **kwargs):
        print(kwargs)
        
        super(ReviewForm,self).__init__(*args, **kwargs)
        if "prof" in kwargs["initial"]:
            prof = kwargs["initial"].pop("prof")
            self.fields["prof"].queryset = Profs.objects.filter(id=prof.id)
            # print(self.fields["prof"].queryset)
            self.fields["course"].queryset = prof.dept.courses_set.all()
        
        if "course" in kwargs["initial"]:
            course = kwargs["initial"].pop("course")
            self.fields["course"].queryset = Courses.objects.filter(id=course.id)
            self.fields["prof"].queryset = course.dept.profs_set.all()
        

class AuthenticationFormCheckBanned(AuthenticationForm):
    def confirm_login_allowed(self, user):
        bl = user.banned_set.all()
        if (bl and "Free" not in bl[0].time_to_relieve):
            msg = "Your account has been banned "
            if("permanent" in bl[0].time_to_relieve):
                msg += "PERMANENTLY"
            else:
                msg += "for " + bl[0].time_to_relieve
            raise forms.ValidationError(
                (msg),
                code='inactive',
            )
