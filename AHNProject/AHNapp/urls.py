from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('services', views.services, name='services'),
    path('courses', views.courses, name='courses'),
    path('drop_course/<int:course_id>/', views.drop_course, name='drop_course'),
    path('add_course/<int:course_id>/', views.add_course, name='add_course'),

    path('login_user', views.login_user, name='login_user'), 
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    

    path('fees',views.fees,name='fees'),
    path('profile',views.profile,name='profile'),
    path('services',views.services,name='services'),
    path('getpdf',views.getpdf,name='getpdf'),

    # path('fees', views.fees, name='fees'),
    # path('profile', views.profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
