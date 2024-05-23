from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, Cart

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
    cart_items = Cart.objects.filter(session_key=request.session.session_key)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

@csrf_exempt
def add_to_cart(request, product_id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, id=product_id)
            quantity = int(request.POST.get('quantity', 1))
            cart_item, created = Cart.objects.get_or_create(
                session_key=request.session.session_key,
                product=product,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return HttpResponse(status=204)
        except Exception as e:
            return HttpResponse(str(e), status=400)
    else:
        return HttpResponse('Method not allowed', status=405)

def remove_from_cart(request, cart_item_id):
    if request.method == 'POST':
        try:
            cart_item = Cart.objects.get(id=cart_item_id, session_key=request.session.session_key)
            cart_item.delete()
            return HttpResponse(status=204)
        except Cart.DoesNotExist:
            return HttpResponse('Item not found in cart', status=404)
    else:
        return HttpResponse('Method not allowed', status=405)