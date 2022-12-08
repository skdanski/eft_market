from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from core.filters import ProductFilter
def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    return render(request, 'store/category_detail.html',{
        'category': category,
        'products': products
    })

def product_details(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'store/product_detail.html', {
        'product': product
    })

def search(request):
    products = Product.objects.all()
    searchFilter = ProductFilter(request.GET, queryset=products)

    return render(request, 'store/search.html', {
        'searchFilter': searchFilter,
    })