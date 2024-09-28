from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', ]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', ]

class PhotoSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['photo_url']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.photo.url)
        return obj.photo.url
        
class Photo2Serializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Photo_2
        fields = ['photo_url']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.photo.url)
        return obj.photo.url

class Photo3Serializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Photo_3
        fields = ['photo_url']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.photo.url)
        return obj.photo.url

class ProductSerializer(serializers.ModelSerializer):
    img = PhotoSerializer(many=True, read_only=True)
    img2 = Photo2Serializer(many=True, read_only=True)
    img3 = Photo3Serializer(many=True, read_only=True)
    
    # Adding fields for category, subcategory, and brand names
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'description', 'color', 'size', 'category', 'material', 'subcategory', 'brand', 'category_name', 'subcategory_name', 'brand_name', 'img', 'img2', 'img3']