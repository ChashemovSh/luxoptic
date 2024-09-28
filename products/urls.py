from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('products/', ProductListView.as_view(), name='product-list'),
]
# from django.urls import path
# from .views import CategoryListView, SubcategoryListView, BrandListView, ProductListView, PhotoListView

# urlpatterns = [
#     path('categories/', CategoryListView.as_view(), name='category-list'),
#     path('subcategories/', SubcategoryListView.as_view(), name='subcategory-list'),
#     path('brands/', BrandListView.as_view(), name='brand-list'),
#     path('products/', ProductListView.as_view(), name='product-list'),
#     path('photos/', PhotoListView.as_view(), name='photo-list'),                  
# ]