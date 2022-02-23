from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=64, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)
    
    username = None

    # which field will be used to login, default is username, changing it to email
    USERNAME_FIELD = 'email'
    # fields which are mandatory for a user to sign up
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    session_token = models.CharField(max_length=10, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

