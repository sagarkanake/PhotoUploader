from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name= 'login'),
    path('register', views.register, name= 'register'),
    path('logout', views.logout_user, name= 'logout'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    path('studentregister', views.studentregister, name= 'studentregister'),
    path('adminregister', views.adminregister, name= 'adminregister'),
    path('teacherregister', views.teacherregister, name= 'teacherregister'),
]
