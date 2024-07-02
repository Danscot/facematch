# image_voting/models.py

from django.db import models


class Image(models.Model):

    name = models.CharField(max_length=100)  # Image file name

    votes = models.IntegerField(default=0)   # Number of votes

    path = models.TextField(max_length=1000)

    def __str__(self):

        return self.name

    @property
    def path(self):
        return f'static/images/{self.name}.png'
