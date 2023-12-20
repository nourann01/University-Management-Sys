from django.shortcuts import render
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
    return render(request, 'courses.html', {'courses': items})

# def fees(request):
#     return render(request, 'AHNapp/fees.html')

# def profile(request):
#     return render(request, 'AHNapp/profile.html')
