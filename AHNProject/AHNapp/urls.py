from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='index'),
    path('home', views.home, name='home'),
    # path('services', views.services, name='services'),
    path('courses', views.courses, name='courses'),
    path('drop_course/<int:course_id>/', views.drop_course, name='drop_course'),
    path('add_course/<int:course_id>/', views.add_course, name='add_course'),

    path('login_user', views.login_user, name='login_user'), 
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register'),
    
    # path('fees', views.fees, name='fees'),
    # path('profile', views.profile, name='profile'),
]
