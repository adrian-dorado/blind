from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField()
    phone_number = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.email}"

