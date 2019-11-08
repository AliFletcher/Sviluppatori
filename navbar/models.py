from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class NewUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    department = models.CharField(max_length=264)
    name = models.CharField(max_length=264)
    course_number = models.CharField(max_length=264)
    group_number = models.CharField(max_length=264)
    teacher = models.CharField(max_length=264)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.CharField(max_length=264)
    second_day = models.CharField(max_length=264, blank=True)
