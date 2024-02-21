from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product




class ProductListView(ListView):
    paginate_by = 9
    model = Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
