from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
# Renders the login form
def sign_in(request):
    if request.method == 'GET':
        # redirect user to posts when they log in
        if request.user.is_authenticated:
            return redirect('posts')
        
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

        #handle the login action
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')
        # form is not valid, wrong username/password
        messages.error(request, f'Invalid Username/Password')
        return render(request, 'users/login.html', {'form': form})

# Logout view
def sign_out(request):
    logout(request)
    messages.success(request, f'You have been successfully logged out')
    return redirect('login')

# register view
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form})
    
    # handle posting
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You signed up successfully.')
            login(request, user)
            return redirect('posts')
        
        else:
            return render(request, 'users/register.html', {'form':form})
