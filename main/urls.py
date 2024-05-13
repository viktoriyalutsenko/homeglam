from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),  # Путь для страницы главная
    path('contacts/', views.contacts, name='contacts'),
]