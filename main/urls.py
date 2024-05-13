from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),  # Путь для страницы главная
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
]