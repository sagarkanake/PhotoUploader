from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name= 'login'),
    path('register', views.register, name= 'register'),
    path('logout', views.logout_user, name= 'logout'),
    path('admindashboard', views.admindashboard, name= 'admindashboard'),
    path('studentdashboard', views.studentdashboard, name= 'studentdashboard'),
    path('teacherdashboard', views.teacherdashboard, name= 'teacherdashboard'),
    path('studentregister', views.studentregister, name= 'studentregister'),
    path('adminregister', views.adminregister, name= 'adminregister'),
    path('teacherregister', views.teacherregister, name= 'teacherregister'),
]
