from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name=models.CharField(max_length=255)
    course_fee=models.IntegerField()
    def __str__(self):
        return self.course_name

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255) 
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField(null=True, blank=True,default=1) 
    joining_date=models.DateField() 

class userteacher(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    mobile=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to="image/", null=True)
# Create your models here.
