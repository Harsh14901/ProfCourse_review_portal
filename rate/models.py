from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Review(models.Model):
    username = models.CharField(max_length=50)
    actual_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.CharField(max_length=1024)
    isAnonymous = models.BooleanField(default=False)
    
    prof = models.ForeignKey("Profs", on_delete=models.CASCADE)
    course = models.ForeignKey("Courses", on_delete=models.CASCADE)
    
    difficulty =models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)],default=0)
    content_quality = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)],default=0)
    grading = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)],default=0)
    attendance = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)],default=0)
    overall_rating = models.IntegerField(validators=[MinValueValidator(0),
                                                     MaxValueValidator(5)], default=0)


class Profs(models.Model):
    dept = models.ForeignKey("Dept", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    webpage = models.URLField(max_length=200)
    pic_url = models.URLField(max_length=200)

    def __str__(self):
        return f"Dept -> {self.dept.name} | Name -> {self.name}"
    


class Courses(models.Model):
    dept = models.ForeignKey("Dept", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code
    






