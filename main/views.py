from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, Cart, FeedbackMessage, Order, OrderItem
from django.core.mail import send_mail

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

    if request.method == 'POST':
        customer_name = request.POST.get('first_name')
        customer_email = request.POST.get('email')

        # Создание нового заказа
        order = Order.objects.create(
            user=request.user,
            customer_name=customer_name,
            customer_email=customer_email,
            total_price=total_price
        )

        # Создание записей OrderItem для каждого товара в корзине
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity
            )

        # Очистка корзины
        Cart.objects.filter(session_key=request.session.session_key).delete()

        # Перенаправление на главную страницу
        return redirect('glavnaya')

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

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Сохранение сообщения в базе данных
        feedback_message = FeedbackMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        feedback_message.save()

        # Отправка ответа на почту
        response_message = "Спасибо за ваше сообщение! Мы рассмотрим его в ближайшее время и свяжемся с вами."
        send_mail(
            subject="Ответ на ваше сообщение",
            message=response_message,
            from_email="hghomeglam@gmail.com",
            recipient_list=[email],
        )

        # Перенаправление на страницу контактов после отправки формы
        return redirect('contacts')

    return render(request, 'contacts.html')