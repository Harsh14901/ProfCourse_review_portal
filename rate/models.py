from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Review(models.Model):


    RatingChoices = (
        (0, "Poor"),
        (1, "Bad"),
        (2, "Average"),
        (3, "Above Average"),
        (4, "Good"),
        (5, "Excellent"),
    )

    # username = models.CharField(max_length=50)
    # actual_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False,null=True)

    comment = models.TextField(max_length=4096)
    isAnonymous = models.BooleanField(default=False,verbose_name="Remain Anonymous?")
    
    prof = models.ForeignKey("Profs", on_delete=models.CASCADE,null=True)
    course = models.ForeignKey("Courses", on_delete=models.CASCADE,null=True)
    
    difficulty = models.IntegerField(choices = RatingChoices,default=0)
    content_quality =models.IntegerField(choices = RatingChoices,default=0)
    grading = models.IntegerField(choices = RatingChoices,default=0)
    attendance = models.IntegerField(choices = RatingChoices,default=0)
    overall_rating =models.IntegerField(choices = RatingChoices,default=0)

    def __str__(self):
        p_name=""
        c_name=""
        if self.prof is None:
            p_name = "None"
        else:
            p_name = self.prof.name
        if self.course is None:
            c_name = "None"
        else:
            c_name = self.course.code
        
        return f"Prof - {p_name} | Course - {c_name} | Rating - {str(self.overall_rating)}"
        
    


class Profs(models.Model):
    dept = models.ForeignKey("Dept", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    webpage = models.URLField(max_length=200)
    # pic_url = models.URLField(max_length=200)

    def __str__(self):
        return f"Dept -> {self.dept.name} | Name -> {self.name}"
    


class Courses(models.Model):
    dept = models.ForeignKey("Dept", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code
    






