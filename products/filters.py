# products/filters.py
import django_filters
from .models import Product, Category, Subcategory, Brand

class ProductFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategory = django_filters.ModelChoiceFilter(queryset=Subcategory.objects.all(), required=False)
    brand = django_filters.ModelChoiceFilter(queryset=Brand.objects.all(), required=False)
    material = django_filters.CharFilter(lookup_expr='icontains')  # Поиск по материалу (без учета регистра)
    size = django_filters.CharFilter(lookup_expr='exact')  # Точный поиск по размеру
    color = django_filters.CharFilter(lookup_expr='exact')  # Точный поиск по цвету
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')  # Filter for minimum price
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')  # Filter for maximum price


    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'brand', 'material', 'size', 'color', 'min_price', 'max_price']

