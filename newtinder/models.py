from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings


class Profile(AbstractUser):
    choices = (
        ('male', 'male'),
        ('female', 'female'),
    )
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, choices=choices, default='male')
    avatar = models.ImageField(upload_to="static/images/avatars/", null=True, blank=True,
                               default='static/images/logo.jpg')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like")

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        with Image.open(self.avatar.path) as img:

            width, height = img.size
            logo = Image.open("static/images/logo.jpg")
            size = (100, 100)
            logo.thumbnail(size)

            x = 0
            y = 0

            x = width - 100
            y = height - 100

            img.paste(logo, (x, y))
            img.save(self.avatar.path)
