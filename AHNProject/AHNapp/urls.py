from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    # path('services', views.services, name='services'),
    path('courses', views.courses, name='courses'),
    path('drop_course/<int:course_id>/', views.drop_course, name='drop_course'),
    path('add_course/<int:course_id>/', views.add_course, name='add_course'),

    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('fees', views.fees, name='fees'),
    # path('profile', views.profile, name='profile'),
]
