from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'accounts/login.html', {'error_message': error_message})   

def logout_user(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request,'accounts/home.html', {'username' : request.user.username})   
  
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
            form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})    
