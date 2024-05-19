from django.shortcuts import render, get_object_or_404
from .models import Category
# Create your views here.
def glavnaya(request):
    return render(request, 'glavnaya.html')

def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

# Create your views here.
def catalog(request):
    categories = Category.objects.all()[:4]  # Получаем первые 4 категории
    context = {
        'categories': categories
    }
    return render(request, 'catalog.html', context)

def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'category': category
    }
    return render(request, 'category_page.html', context)