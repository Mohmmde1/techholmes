from django.urls import path

from cart.views import add_to_cart, update_cart

urlpatterns = [
    path('', add_to_cart, name='cart'),
    path('update_cart', update_cart, name='update_cart')
]
