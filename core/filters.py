import django_filters
from store.models import *
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
    # Allows searching with partially matching field (product title)
    name = CharFilter(label='Name', field_name='title', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['category','name','price']
    