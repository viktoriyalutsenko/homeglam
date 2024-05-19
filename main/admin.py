from django.contrib import admin
from .models import Admin, Category, Product

admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Product)