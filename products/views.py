from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .models import Category, Subcategory, Brand, Product
from .serializers import CategorySerializer, SubcategorySerializer, BrandSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import ProductFilter



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter  # Connect the filter

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if query is not None:
            products = self.queryset.filter(name__icontains=query)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Please provide a search query"}, status=400)

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_order = self.request.query_params.get('sort', None)
        if sort_order == 'price_asc':
            queryset = queryset.order_by('price')  # Sort by ascending price
        elif sort_order == 'price_desc':
            queryset = queryset.order_by('-price')  # Sort by descending price
        return queryset

    @action(detail=False, methods=['get'])
    def by_id(self, request):
        product_id = request.query_params.get('id', None)
        if product_id is not None:
            # Найдем объект продукта по id или вернем 404, если продукт не найден
            product = get_object_or_404(Product, id=product_id)
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        return Response({"error": "Please provide a valid product ID"}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
# from rest_framework import generics
# from .models import Category, Subcategory, Brand, Product, Photo
# from .serializers import CategorySerializer, SubcategorySerializer, BrandSerializer, ProductSerializer, PhotoSerializer

# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class SubcategoryListView(generics.ListAPIView):
#     queryset = Subcategory.objects.all()
#     serializer_class = SubcategorySerializer

# class BrandListView(generics.ListAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class PhotoListView(generics.ListAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer