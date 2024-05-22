from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


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

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.image)
            image.thumbnail((250, 250), resample=Image.BICUBIC)
            output = BytesIO()
            image.save(output, format='PNG', optimize=True, transparent=True)
            self.image.save(self.image.name, ContentFile(output.getvalue()), save=False)
        super().save(*args, **kwargs)

class Cart(models.Model):
    session_key = models.CharField(max_length=40)
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)