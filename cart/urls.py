from django.urls import path

from cart.views import add_to_cart

urlpatterns = [
    path('', add_to_cart, name='cart'),
]
