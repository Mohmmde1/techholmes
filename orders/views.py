from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from cart.models import Cart
from .models import Order, OrderItem


def get_cart(request):
    # Attempt to get the cart for the current user
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # If the cart doesn't exist for the user, create a new one
        cart = Cart.objects.create(user=request.user)
    return cart

@login_required
def make_order(request):
    # Get the cart for the current user
    cart = get_cart(request)

    if len(cart.items.all()) == 0:
        return redirect('cart')

     # Create an order based on the cart
    order = Order.objects.create(
         user=request.user,
         total=cart.total,
     )
    order_items = []
    for cart_item in cart.items.all():
        order_items.append(OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity
        ))


    # You may want to clear the cart after creating the order
    cart.items.all().delete()

    return render(request, 'orders/order_details.html', {"order": order})

@login_required
def display_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {"orders": orders})
