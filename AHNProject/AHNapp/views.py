from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Course, User, Student, Advisor
# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'homepage.html')

# def services(request):
#     return render(request, 'AHNapp/services.html')

def courses(request):
    items = Course.objects.all()
    advisorat = Advisor.objects.all()
    total_weight = Course.objects.all().filter(isReg=True).aggregate(Sum('CourseWeight'))['CourseWeight__sum']
    regis_num = Course.objects.filter(isReg=True).count()
    return render(request, 'courses.html', {'courses': items,'total_weight': total_weight,"regis_num":regis_num,'advisorat':advisorat})


def drop_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.isReg = False
    course.save()
    return redirect('courses')
# def fees(request):
#     return render(request, 'AHNapp/fees.html')

# def profile(request):
#     return render(request, 'AHNapp/profile.html')
