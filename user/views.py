from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Login !')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        confirm_password = request.POST.get('confirm-password')
        if password != confirm_password:
            messages.info(request, 'Your Password And Confirm Password Should Be Same!')
            return render(request, 'register.html')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Already Exist!')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(first_name=name, username=username, password=password)
                user.save()
                return redirect('login')
    else:
        return render(request, 'register.html', {})


def user_logout(request):
    logout(request)
    return redirect('index')
