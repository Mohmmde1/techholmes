from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from products.models import Product

from .models import Cart, CartItem
from .forms import AddCartForm

def get_cart(request):
    # Attempt to get the cart for the current user
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # If the cart doesn't exist for the user, create a new one
        cart = Cart.objects.create(user=request.user)
    return cart

@login_required
def add_to_cart(request):
    cart = get_cart(request)



    if request.method == 'POST':
        form = AddCartForm(data=request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            slug = form.cleaned_data['slug']
            product = get_object_or_404(Product, slug=slug)
            # Check if the item already exists in the cart
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            # Update quantity if the item already exists, otherwise create a new cart item
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
            return render(request, 'cart/cart.html', {"cart":cart})


    return render(request, 'cart/cart.html', {"cart":cart})


@login_required
def update_cart(request):
    cart = get_cart(request)

    if request.method == 'POST':
        for item in cart.items.all():
            quantity_key = f'quantity_{item.id}'
            if quantity_key in request.POST:
                quantity = int(request.POST[quantity_key])
                if quantity > 0:
                    item.quantity = quantity
                    item.save()
                else:
                    item.delete()

    return HttpResponseRedirect('/cart/')
