from django.contrib import admin
from image_uploader_widget.admin import ImageUploaderInline
from .models import *

class PhotoInline(ImageUploaderInline):
    model = Photo

class Photo_2Inline(ImageUploaderInline):
    model = Photo_2

class Photo_3Inline(ImageUploaderInline):
    model = Photo_3

class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'price', 'description', 'category', 'material')  # Fields to display
  inlines = [PhotoInline, Photo_2Inline, Photo_3Inline]

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the list view

admin.site.register(Subcategory, SubcategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the list view

admin.site.register(Brand, BrandAdmin)


  