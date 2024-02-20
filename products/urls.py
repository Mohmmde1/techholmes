from django.urls import path

from products.views import product_detail, product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]