from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Course, User, Student, Advisor

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'message': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')

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
