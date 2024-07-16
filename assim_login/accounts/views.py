# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserForm, ProfileForm
from .models import CustomUser

def home(request):
    return render(request, 'accounts/home.html')
    
def signup_step1(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            request.session['user_data'] = form.cleaned_data
            return redirect('signup_step2')
    else:
        form = UserForm()
    return render(request, 'accounts/signup_step1.html', {'form': form})

def signup_step2(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_data = request.session['user_data']
            user = CustomUser.objects.create_user(
                username=user_data['username'],
                password=user_data['password1'],
                email=user_data['email']
            )
            user.phone_number = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            user.save()
            return redirect('login')
    else:
        form = ProfileForm()
    return render(request, 'accounts/signup_step2.html', {'form': form})

def signup_step3(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_data = request.session['user_data']
            user = CustomUser.objects.create_user(
                username=user_data['username'],
                password=user_data['password1'],
                email=user_data['email']
            )
            user.phone_number = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            user.save()
            return redirect('login')
    else:
        form = ProfileForm()
    return render(request, 'accounts/signup_step3.html', {'form': form})
def congratulations(request):
    return render(request, 'accounts/congratulations.html')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts-home')
    return render(request, 'registration/logout.html')