from django import forms 
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image', 'trade_location', 'phone_num', 'deadline',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'trade_location': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'phone_num': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),

        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image', 'trade_location', 'phone_num')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'phone_num': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'trade_location': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }

