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
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)

    comment = models.TextField(max_length=4096)
    isAnonymous = models.BooleanField(default=False,verbose_name="Remain Anonymous?")
    
    prof = models.ForeignKey("Profs", on_delete=models.CASCADE,null=True)
    course = models.ForeignKey("Courses", on_delete=models.CASCADE,null=True)
    
    difficulty = models.IntegerField(choices = RatingChoices,default=0)
    content_quality =models.IntegerField(choices = RatingChoices,default=0)
    grading = models.IntegerField(choices = RatingChoices,default=0)
    attendance = models.IntegerField(choices = RatingChoices,default=0)
    overall_rating =models.IntegerField(choices = RatingChoices,default=0)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    
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
   
class Warnings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


class Banned(models.Model):
    PERMANENT = "Banned Permanently"
    FREE = "Free to relieve"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ban_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    ban_duration = models.DurationField(null=True)
    permanent_ban = models.BooleanField(default=False)

    @property
    def ban_relieve(self):
        if(not self.permanent_ban):
            return self.ban_date + self.ban_duration
        else:
            return self.PERMANENT

    @property
    def time_to_relieve(self):
        if(not self.permanent_ban):
            if(self.ban_relieve > dt.today()):
                a = self.ban_relieve - dt.today()
                return f"{a.days} days,{a.seconds//3600} hours"
            else:
                return self.FREE
        else:
            return self.PERMANENT
    
    def __str__(self):
        return self.user.__str__()
    

class Activity(models.Model):
    LIKE = "Like"
    DISLIKE = "Disike"
    SIGNUP = "Signup"
    LOGIN = "Login"
    LOGOUT = "Logout"
    COMMENT = "Comment"
    REPORT = "Report"
    CategoryChoices = (
        (COMMENT,"Comment"),
        (REPORT,"Report"),
        (LOGIN,"Login"),
        (LOGOUT,"Logout"),
        (SIGNUP,"Signup"),
        (LIKE,"Like"),
        (DISLIKE,"Dislike"),
    )

    category = models.CharField(choices=CategoryChoices, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    log = models.TextField(null=True)
    def __str__(self):
        return f"{self.category} | user : {self.user}"

    def login_log(self):
        self.log = f"{self.user} Logged in "
    
    def signup_log(self):
        self.log = f"{self.user} Signed up "

    def logout_log(self):
        self.log = f"{self.user} Logged out "

    def comment_log(self,review):
        self.log = f"{self.user} added a comment to {review.prof} and {review.course} with comment {review.comment}"

    def report_log(self,report):
        self.log = f"{self.user} reported a comment by {report.reported_user} on prof {report.review.prof} and course {report.review.course}"

    def like_log(self,review):
        self.log = f"{self.user} Liked a comment by {review.user} on prof {review.prof.name} and course {review.course.code}"

    def dislike_log(self,review):
        self.log = f"{self.user} Disliked a comment by {review.user} on prof {review.prof.name} and course {review.course.code}"

     
class Credibility(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    trust = models.IntegerField(default=0)

    def __str__(self):
        return f"User - {self.user} | Trust {self.trust}"
    
