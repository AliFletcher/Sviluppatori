from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    user_name = models.CharField(max_length=264)
    email = models.EmailField()
    password = models.CharField(max_length=264)
    verify_password = models.CharField(max_length=264)
