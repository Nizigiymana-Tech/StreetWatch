from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name="")
def main_view(request):
    current_user = request.user
    
    if request.method == "POST":
        if "Profile" in request.POST:
            return redirect('profile')
        
        if "Settings" in request.POST:
            return redirect('settings')
        
    return render(request, "homepage.html", {"user": current_user})