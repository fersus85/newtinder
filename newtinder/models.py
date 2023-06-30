from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    choices = (
        ('male', 'male'),
        ('female', 'female'),
    )
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, choices=choices, default='male')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
