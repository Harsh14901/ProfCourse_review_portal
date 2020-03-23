from django.contrib.auth.forms import AuthenticationForm
from django import forms
from rate.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Email is Required")
    first_name = forms.CharField(max_length=50, required=False,help_text="Optional")
    last_name = forms.CharField(max_length=50, required=False, help_text="Optional")

    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')

    def save(self, commit=True):
        user = super().save(commit=commit)
        return user

    def is_valid(self):
        valid = super().is_valid()
        
        if not valid:
            return valid
        
        email = self.cleaned_data['email']
        r1 = re.compile('(.*)@.*iitd.ac.in')
        match = r1.search(email)
        if(match is None):
            self._errors[''] = "This portal is only for IITD students. Trespassers will be hacked!!"
            return False
        kerb_id = match.groups(1)[0]
        users = User.objects.filter(email__endswith="iitd.ac.in").filter(email__startswith=kerb_id)
        if (len(users) != 0):
            print(users)
            self._errors[''] = "This email address already exists. Try fooling someone else!!"
            return False

        return valid


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
        if (bl and bl[0].time_to_relieve != Banned.FREE):
            msg = "Your account has been banned "
            if("permanent" in bl[0].time_to_relieve):
                msg += "PERMANENTLY"
            else:
                msg += "for " + bl[0].time_to_relieve
            raise forms.ValidationError(
                (msg),
                code='inactive',
            )
        else:
            if bl:
                bl[0].delete()
            login_activity = Activity(user=user,category=Activity.LOGIN)
            login_activity.login_log()
            login_activity.save()
