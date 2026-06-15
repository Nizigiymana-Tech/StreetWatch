from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='static/profile_images')
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    
class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="settings")

    street_address = models.CharField(max_length=255, default="1 Officer Manny Familia Wy")
    city = models.CharField(max_length=100, default="Worcester")
    state = models.CharField(max_length=50, default="MA")
    zip_code = models.CharField(max_length=10, blank=True, null=True, default="01605")
    coordinatesx = models.CharField(blank=True, null=True)
    coordinatesy = models.CharField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username # type: ignore 