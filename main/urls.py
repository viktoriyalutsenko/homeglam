from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),  # Путь дла страницы главная
]