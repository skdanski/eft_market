from django.shortcuts import render
from store.models import Product


def mainpage(request):
    products = Product.objects.all()[0:4]
    return render(request, 'core/mainpage.html', {
        'products': products
    })