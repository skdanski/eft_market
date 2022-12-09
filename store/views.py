from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from core.filters import ProductFilter


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)

    return render(request, 'store/category_detail.html',{
        'category': category,
        'products': products
    })

def product_details(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {
        'product': product
    })

def search(request):
    products = Product.objects.filter(status=Product.ACTIVE)
    searchFilter = ProductFilter(request.GET, queryset=products)

    return render(request, 'store/search.html', {
        'searchFilter': searchFilter,
    })