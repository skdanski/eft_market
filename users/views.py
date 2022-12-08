from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserProfile

def seller_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'users/seller_detail.html', {
        'user': user
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