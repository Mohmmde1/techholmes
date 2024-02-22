from django.shortcuts import render, get_object_or_404

from django_filters.views import FilterView
from products.filters import ProductFilter
from .models import Product




class ProductListView(FilterView):
    paginate_by = 9
    filterset_class = ProductFilter
    template_name = 'products/product_list.html'
    

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
