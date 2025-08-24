from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')

def desenvolvimento(request):
        return render(request, 'desenvolvimento.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm