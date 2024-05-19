from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:category_id>/', views.category_page, name='catalog-page'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]