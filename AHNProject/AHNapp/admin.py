from django.contrib import admin
from .models import User, Student, Advisor,Course
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Advisor)
admin.site.register(Course)