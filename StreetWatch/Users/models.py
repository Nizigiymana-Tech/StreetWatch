from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='static/profile_images')
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.user.username