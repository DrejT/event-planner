from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class UserPost(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=600)
    slug = models.SlugField(max_length=400)
    address = models.CharField(max_length=200)
    social = models.URLField(max_length=200, blank=True, null=True)
