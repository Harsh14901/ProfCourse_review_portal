from django import forms
from rate.models import *
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
        
        
