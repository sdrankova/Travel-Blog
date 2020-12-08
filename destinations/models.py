from django.db import models

# Create your models here.
from accounts.models import UserProfile


class Destination(models.Model):
    title = models.CharField(max_length=50, blank=False)
    destination = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='destinations',
    )

    current_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Like(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    current_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    current_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
