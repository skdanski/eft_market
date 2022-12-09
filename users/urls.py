from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('sell/', views.mystore, name='sell'),
    path('sell/add_product/', views.add_product, name='add_product'),
    path('sell/edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('sell/delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sellers/<int:pk>/', views.seller_detail, name="seller_detail"),
]
