from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

# MainPage

@login_required(redirect_field_name="")
def main_view(request):
    return render(request, "homepage.html")