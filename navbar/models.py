from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    username = models.CharField(max_length=264)
    email = models.EmailField()
    password1 = models.CharField(max_length=264)
    password2 = models.CharField(max_length=264)
