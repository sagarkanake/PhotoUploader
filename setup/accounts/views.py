from django.shortcuts import redirect, render
from django.shortcuts import render, HttpResponseRedirect

from django.contrib.auth import logout 
# from .forms import StudentRegistration,UserLogin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Student, Teacher, Admin
# from django.contrib.auth.models import CustomUser
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from .models import Image
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.error(request, 'Your are Logged in')
            if user.is_admin == True:
             return redirect('admindashboard')
            if user.is_student == True:
             return redirect('studentdashboard')
            if user.is_teacher == True:
             return redirect('teacherdashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')    
    
        
        
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username exists')
                return redirect('register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = CustomUser.objects.create_user(first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                    
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
        
        
        
    return render(request, 'accounts/register.html')
def studentregister(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        standard = request.POST['standard']
        add = request.POST['add']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username exists')
                return redirect('studentregister')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('studentregister')
                else:
                    user = CustomUser.objects.create_user(is_student = True, first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
                    user.save()
                    student = Student.objects.create(user = user , standard = standard, add = add)
                    student.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                    
        else:
            messages.error(request, 'Password do not match')
            return redirect('studentregister')
        
    return render(request, 'accounts/studentregister.html')

def teacherregister(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        add = request.POST['add']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username exists')
                return redirect('teacheradminregister')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('teacheradminregister')
                else:
                    user = CustomUser.objects.create_user(is_teacher = True,first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
                    user.save()
                    student = Teacher.objects.create(user = user , subject = subject, add = add)
                    student.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                    
        else:
            messages.error(request, 'Password do not match')
            return redirect('teacherregister')
        
    return render(request, 'accounts/teacherregister.html')

def adminregister(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        add = request.POST['add']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username exists')
                return redirect('adminregister')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('adminregister')
                else:
                    user = CustomUser.objects.create_user(is_admin= True,first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
                    user.save()
                    student = Admin.objects.create(user = user , add = add)
                    student.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                    
        else:
            messages.error(request, 'Password do not match')
            return redirect('adminregister')
        
    return render(request, 'accounts/adminregister.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def admindashboard(request):
    
        email = request.user
        user = CustomUser.objects.get(email = email)
        username = user.first_name
        
        alladmins = CustomUser.objects.filter(is_admin = True)
        admins = Image.objects.filter(user__in = alladmins).order_by('date')
        
        allteachers = CustomUser.objects.filter(is_teacher = True)
        teachers = Image.objects.filter(user__in = allteachers).order_by('date')
        
        allstudents = CustomUser.objects.filter(is_student = True)
        students = Image.objects.filter(user__in = allstudents).order_by('date')
        
        data = {
            'username' : username,
            'admins' : admins, 
            'teachers' : teachers, 
            'students' : students,
        }
        
        if request.method == 'POST':
            
            prod = Image()
            prod.user = request.user
            if len(request.FILES) != 0:
             prod.photo = request.FILES['image']

             prod.save()
             messages.success(request, "Product Added Successfully")
            return render(request, 'accounts/admindashboard.html' , data )
        return render(request, 'accounts/admindashboard.html' , data )
    
@login_required(login_url='login') 
def teacherdashboard(request):    
        name = request.user
        ex = CustomUser.objects.get(email=name)
        username = ex.first_name
        teachers = Image.objects.filter(user = request.user)
        all = CustomUser.objects.filter(is_student = True)
        students = Image.objects.filter(user__in = all)
        data = {
            'teachers' : teachers,
            'username' : username,
            'students' : students,
        }
        if request.method == 'POST':
            prod = Image()
            prod.user = request.user
            if len(request.FILES) != 0:
             prod.photo = request.FILES['image']
             prod.save()
             messages.success(request, "Product Added Successfully")
            return render(request, 'accounts/teacherdashboard.html' , data )
        return render(request, 'accounts/teacherdashboard.html' , data )

@login_required(login_url='login')    
def studentdashboard(request):
        name = request.user
        ex = CustomUser.objects.get(email=name)
        username = ex.first_name
        students = Image.objects.filter(user=request.user)
        data = {
            'students' : students,
            'username' : username,
        }
        if request.method == 'POST':
            prod = Image()
            prod.user = request.user
            if len(request.FILES) != 0:
             prod.photo = request.FILES['image']
             prod.save()
             messages.success(request, "Product Added Successfully")
            return render(request, 'accounts/studentdashboard.html' , data  )
        return render(request, 'accounts/studentdashboard.html' , data )
        
  
    

