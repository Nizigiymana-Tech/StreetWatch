from django import forms
from django.contrib.auth import get_user_model, authenticate
from .models import UserProfile, UserSetting

User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        

        help_texts = {
            'username': "",
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid username or password.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")
        return cleaned_data
    
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']
        
    # super is the the parent class that allows you to use functions inside the parent class inside the child class
    # args are tuple '()' that have int values, strings etc, kwargs are dictionaries '[]' 
    # EXAMPLE: (chatgpt)

    # def multiply_all(*args):
    # # args is collected into a tuple: (2, 3, 4)
    #   result = 1
    #   for num in args:
    #     result *= num
    #   return result

    # print(multiply_all(2, 3))        # Output: 6
    # print(multiply_all(2, 3, 4, 5))  # Output: 120

    # def print_profile(**kwargs):
    #   # kwargs is collected into a dictionary: {"name": "Alice", "role": "Dev"}
    #    for key, value in kwargs.items():
    #       print(f"{key}: {value}")

    # Pass inputs using key=value syntax
    #   print_profile(name="Alice", role="Developer", city="Boston")
    # Output:
    # name: Alice
    # role: Developer
    # city: Boston

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].required = False

class SettingsForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['street_address', 'city', 'state', 'zip_code', "coordinatesx", "coordinatesy"]