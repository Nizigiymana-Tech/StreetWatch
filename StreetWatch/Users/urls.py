from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('signup/', views.signup, name="signup"),
]