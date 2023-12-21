from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Course, User, Student, Advisor
from django.contrib.auth.models import User
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create Student object
            Student.objects.create(user=user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], major=request.POST['major'], study_year=request.POST['study_year'])
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'message': 'Invalid login credentials'})
    else:
        return render(request, 'index.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    else:
        return render(request, 'index.html')
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

def add_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.isReg = True
    course.save()
    return redirect('courses')
# def fees(request):
#     return render(request, 'AHNapp/fees.html')

# def profile(request):
#     return render(request, 'AHNapp/profile.html')
