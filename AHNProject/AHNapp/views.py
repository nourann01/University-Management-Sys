from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'AHNapp/index.html')

def home(request):
    return render(request, 'AHNapp/home.html')

def services(request):
    return render(request, 'AHNapp/services.html')

def courses(request):
    return render(request, 'AHNapp/courses.html')

def fees(request):
    return render(request, 'AHNapp/fees.html')

def profile(request):
    return render(request, 'AHNapp/profile.html')