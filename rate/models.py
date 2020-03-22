from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime as dt
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
        
        return f"Prof - {p_name} | Course - {c_name} | Rating - {str(self.overall_rating)} | User - {self.user.username}"
        
    


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

class ReportReview(models.Model):
    SPAM = "Spam"
    FRAUD = "Fraud"
    OFFENSIVE = "Offensive"

    CategoryChoices = (
        (SPAM, "Spam"),
        (FRAUD, "Fraud"),
        (OFFENSIVE, "Offensive"),
    )

    review = models.ForeignKey("Review", on_delete=models.CASCADE)
    reporting_user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CategoryChoices)
    reason = models.TextField(verbose_name="Please specify any other details", max_length=5000)

    def __str__(self):
        return f"Category : {self.category} | Reported User : {self.review.user.username}" 
    
    @property
    def reported_user(self):
            return self.review.user


# class Activity(models.Model):
#     COMMENT = "Comment"
#     REPORT = "Report"
#     CategoryChoices = (
#         (COMMENT,"Comment"),
#         (REPORT,"Report"),
#     )

#     category = models.CharField(choices=CategoryChoices, max_length=50)
#     review = models.ForeignKey("Review", on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.category} | Review : {self.review}"
    
class Warnings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


class Banned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ban_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    ban_duration = models.DurationField(null=True)
    permanent_ban = models.BooleanField(default=False)

    @property
    def ban_relieve(self):
        if(not self.permanent_ban):
            return self.ban_date + self.ban_duration
        else:
            return "Banned Permanently"

    @property
    def time_to_relieve(self):
        if(not self.permanent_ban):
            return str((self.ban_relieve - dt.today()).days) + " days"
        else:
            return "Banned permanently"
    
    def __str__(self):
        return self.user.__str__()
    






