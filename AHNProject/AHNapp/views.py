from django.shortcuts import render
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
    total_weight = Course.objects.all().aggregate(Sum('CourseWeight'))['CourseWeight__sum']
    regis_num = Course.objects.filter(isReg=True).count()
    return render(request, 'courses.html', {'courses': items,'total_weight': total_weight,"regis_num":regis_num})

# def fees(request):
#     return render(request, 'AHNapp/fees.html')

# def profile(request):
#     return render(request, 'AHNapp/profile.html')
