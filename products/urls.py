from django.urls import path

from products.views import product_detail, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]