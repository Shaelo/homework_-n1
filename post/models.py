from django.db import models

# Create your models here.
from django.db.models import Model


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} \n {self.description}'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title