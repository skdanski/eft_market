from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from .models import UserProfile
from store.forms import EditProductForm, AddProductForm
from store.models import Product


def seller_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)

    return render(request, 'users/seller_detail.html', {
        'user': user,
        'products': products
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            user = UserProfile.objects.create(user=user)
            return redirect('mainpage')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/signup.html', {
        'form': form
    })

def myaccount(request):
    return render(request, 'users/myaccount.html')

def mystore(request):
    if request.user.is_authenticated == False:
        return render(request, 'users/sell.html')
    
    products = request.user.products.exclude(status=Product.DELETED)

    return render(request, 'users/sell.html', {
        'products': products
    })

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'Product Successfully Added!')

            return redirect('sell')
    else:
        form = AddProductForm()

    return render(request, 'users/add_product.html', {
        'form': form,
        'title': 'Add Product'
    })

def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Product Successfully Edited!')
            return redirect('sell')

    else:
        form = EditProductForm(instance=product)

    return render(request, 'users/add_product.html', {
        'form': form,
        'title': 'Edit Product',
        'product': product
    })

def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()
    messages.success(request, 'Product Successfully Deleted!')
    return redirect('sell')