from django.shortcuts import render, redirect
from .forms import UserForm, LoginUserForm

# Create your views here.

# Main signup page
def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    return render(request, "signup.html", {'forms': form})

# Login Page
def login_view(request):
    if request.method == "POST":
        # form = UserForm(request.POST)

        # if form.is_valid():
        #     form.save()
        #     return redirect('home')
        print("OK")
    else:
        form = LoginUserForm()

    return render(request, "login.html", {'forms': form})