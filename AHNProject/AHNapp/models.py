from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
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
    id = models.AutoField(primary_key=True)
    Studentid = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Studentid')
    CourseTitle = models.CharField(max_length=200)
    CourseCode = models.CharField(max_length=200)
    CourseWeight = models.FloatField()
    CourseGrade = models.FloatField()
    isReg = models.BooleanField(default=False)