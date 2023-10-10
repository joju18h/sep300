from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Cart, CartItem, Order
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Sum, F
from django.db import transaction


def index(request):
    return HttpResponse("Your Estore application is working")

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user
    #get the quantity from the form
    quantity = int(request.POST.get('quantity', 1))

    cart, created = Cart.objects.get_or_create(user=user)

    try:
        # transaction.atomic() context manager ensures that the database operations within
        # its block are either all committed successfully or rolled back entirely if any exception occurs.
        with transaction.atomic():
            cart_item, item_created = CartItem.objects.get_or_create(
                cart=cart, product=product,
                defaults={'quantity': quantity}
            )

            if not item_created:
                cart_item.quantity += quantity
                cart_item.save()
    # was getting an integrity error, hence it had to be handled. Presumably because of multiple get_or_create calls
    except IntegrityError:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

    #Filters cart_items belonging to the currently calling user's cart.
    # The summed quantity by the aggrfeate function is returned as a dictionary
    # accesed using the key 'total_quantity'
    cart_size = CartItem.objects.filter(cart=cart).aggregate(total_quantity=Sum('quantity'))['total_quantity']

    response_context = {
        "success": True,
        "cart_size": cart_size
    }

    return JsonResponse(response_context)




def view_cart(request):
    user_cart_items = CartItem.objects.filter(cart__user=request.user)
    #F model allows the referencing of a model field and perform database operations on it
    total_price = user_cart_items.aggregate(total_price=Sum(F('quantity') * F('product__price')))['total_price']

    context = {
        'cart_items': user_cart_items,
        'total': total_price,
    }
    return render(request, 'cart.html', context)


def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = user_cart.cartitem_set.all()

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(user=request.user, total_price=total_price)
    order.items.set(cart_items)
    order.save()

    cart_items.delete()
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'checkout.html', context)
