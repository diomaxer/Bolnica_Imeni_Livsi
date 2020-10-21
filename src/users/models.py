from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    city = models.CharField(max_length=30, blank=True)
    company = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars')