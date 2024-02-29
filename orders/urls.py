from django.urls import path

from orders.views import make_order, display_orders, display_order

urlpatterns = [
    path('', make_order, name='order'),
    path('/orders', display_orders, name='orders'),
    path('/<slug:slug>/', display_order, name='order')
]
