from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserForm, LoginUserForm

# Create your views here.

# Main signup page
def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()

    return render(request, "signup.html", {'forms': form})

# Login Page
def login_view(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST or None)

        if form.is_valid():
            user = form.user_cache
            login(request, user)
            return redirect('/')
    else:
        form = LoginUserForm()

    return render(request, "login.html", {'forms': form})

# Logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    
    return redirect("signup") 