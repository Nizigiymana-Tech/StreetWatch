from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginUserForm, UpdateProfileForm, UpdateUserForm, SettingsForm
from .models import UserProfile, UserSetting

# Create your views here.

# Main signup page
def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:homepage')
    else:
        form = UserForm()
        
    # Standardized context key to 'form'
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

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def settings(request):
    user_settings, created = UserSetting.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = SettingsForm(request.POST, instance=user_settings)

        if form.is_valid():
            form.save()
            return redirect("home:homepage")
    else:
        form = SettingsForm(instance=user_settings)

    return render(request, "settings.html", {
        "form": form
    })