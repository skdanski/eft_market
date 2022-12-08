from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.category_details, name='category_details'),
    path('<slug:category_slug>/<slug:slug>/', views.product_details, name='product_details'),
]
