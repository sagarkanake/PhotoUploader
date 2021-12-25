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

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.error(request, 'Your are Logged in')
            return redirect('dashboard')
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
                    user = CustomUser.objects.create_user(first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
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
                    user = CustomUser.objects.create_user(first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
                    user.save()
                    student = Student.objects.create(user = user , subject = subject, add = add)
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
                    user = CustomUser.objects.create_user(first_name=firstname, last_name=lastname, username=username, phone_number=phone_number, email=email, password=password)
                    user.save()
                    student = Student.objects.create(user = user , add = add)
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
def dashboard(request):
    email = request.user.email
    username = request.user.username
    firstname = request.user.first_name
    phone_number = request.user.phone_number
    lastname = request.user.last_name
    data = {
        'username' : username,
        'email' : email,
        'phone_number' : phone_number,
        'firstname' : firstname,
        'lastname' : lastname,
    }
    return render(request, 'accounts/dashboard.html', data)