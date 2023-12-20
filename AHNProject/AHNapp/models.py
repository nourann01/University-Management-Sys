from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)



class Student(User):
    GPA = models.FloatField()
    CoursesList = models.TextField()

class Advisor(User):
    position = models.CharField(max_length=200)

class Course(models.Model):
    CourseTitle = models.CharField(max_length=200)
    Courseid = models.AutoField(primary_key=True)
    CourseWeight = models.FloatField()
    CourseGrade = models.FloatField()
    isReg = models.BooleanField(default=False)