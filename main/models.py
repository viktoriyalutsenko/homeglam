from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    # Добавьте дополнительные поля, если необходимо
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories', null=True, blank=True)

    def __str__(self):
        return self.name