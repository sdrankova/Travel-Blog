from django.db import models


# Create your models here.
class Destination(models.Model):
    user = models.CharField(max_length=20, blank=False)
    title = models.CharField(max_length=50, blank=False)
    destination = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='destinations',
    )

    def __str__(self):
        return f'{self.title}'


class Like(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)


class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
