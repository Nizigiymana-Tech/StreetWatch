from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginUserForm, UpdateProfileForm, UpdateUserForm

# Create your views here.

# Main signup page
def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home/')
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

@login_required(redirect_field_name="")
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home:homepage')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
        