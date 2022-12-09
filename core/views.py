from django.shortcuts import render
from store.models import Product


def mainpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:4]
    return render(request, 'core/mainpage.html', {
        'products': products
    })