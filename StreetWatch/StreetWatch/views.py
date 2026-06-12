from django.shortcuts import redirect

def main_view(request):
    user = request.user

    print(user.is_authenticated)

    if user.is_authenticated:
        return redirect("home:homepage")
    
    return redirect("login")
