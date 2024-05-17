from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    # Добавьте дополнительные поля, если необходимо
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)