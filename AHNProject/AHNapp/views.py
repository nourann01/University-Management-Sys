from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Course, User, Student, Advisor
from django.contrib.auth.models import User

from .forms import RegisterUserForm
# Create your views here.


def login_user(request):
    # User fill the form and submit
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "There was an error logging in.")
            return redirect('login_user')
            ...
    # User only viewed page
    else:
        return render(request, 'index.html',{})

def logout_user(request):
    logout(request)
    return redirect('login_user')
    
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # save user to database
            user = form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            # log the user in
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
        
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'homepage.html')

# def services(request):
#     return render(request, 'AHNapp/services.html')

def courses(request):
    items = Course.objects.all()
    advisorat = Advisor.objects.all()
    total_weight = Course.objects.all().filter(isReg=True).filter().aggregate(Sum('CourseWeight'))['CourseWeight__sum']
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
