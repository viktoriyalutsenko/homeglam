from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:category_id>/', views.category_page, name='catalog-page'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)