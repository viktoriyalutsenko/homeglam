from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .models import Cart, Product

def glavnaya(request):
    return render(request, 'glavnaya.html')

def catalog(request):
    categories = Category.objects.all()[:4]
    context = {
        'categories': categories
    }
    return render(request, 'catalog.html', context)

def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'category': category
    }
    return render(request, 'catalog_page.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def cart(request):
    return render(request, 'cart.html')

def cart(request):
    session_key = request.session.session_key
    cart_items = Cart.objects.filter(session_key=session_key)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    cart_item, created = Cart.objects.get_or_create(
        session_key=session_key,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')