from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def userlogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'User logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    return render(request, 'login.html')
    

def user_signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.error(request, 'Password and Confirm Password does not match')
            return redirect('signup')
        try:
            if User.objects.get(email=get_email):
                messages.error(request, 'Email already exists')
                return redirect('signup')
        except:
            pass
        user = User.objects.create_user(username=get_email, email=get_email, password=get_password, first_name=fname, last_name=lname)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('login')
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return render(request, 'login.html')