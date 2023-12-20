from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('services', views.services, name='services'),
    path('courses', views.courses, name='courses'),
    path('fees', views.fees, name='fees'),
    path('profile', views.profile, name='profile'),
]
