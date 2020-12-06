from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='avatars',
        blank=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
