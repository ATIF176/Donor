from email import message
from click import command
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('home')

def activeEmail(request, user, to_email):
    mail_subject = "Activate your Account"
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def userlogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')

        if get_email and get_password:
            myuser = authenticate(username=get_email, password=get_password)
            if myuser is not None:
                login(request, myuser)
                messages.success(request, 'User logged in successfully')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('login')
        else:
            messages.error(request, 'Both email and password are required.')
            return redirect('login')

    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        if not get_password or not get_confirm_password:
            messages.error(request, 'Password is required')
            return redirect('signup')

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
        user.is_active = False
        user.save()
        activeEmail(request, user, get_email)
        return redirect('confirm')
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'User Logout Successfully!')
    return render(request, 'login.html')