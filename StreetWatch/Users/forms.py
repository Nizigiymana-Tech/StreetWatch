from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

        help_texts = {
            'username': "",
        }

    def save(self, commit=True):
        User = super().save(commit=False)
        User.set_password(self.cleaned_data["password"])

        if commit:
            User.save()
        
        return User

class LoginUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'password']

        help_texts = {
            'username': "",
        }
    