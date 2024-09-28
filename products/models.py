from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)  # Category name (up to 50 characters)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)  # Subcategory name (up to 50 characters)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)  # Brand name (up to 50 characters)
   

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=50)  # Product name (up to 50 characters)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Stores price with 2 decimal places
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Скидка в процентах
    description = models.TextField()  # Stores product description
    color = models.CharField(max_length=50)  # Stores color (up to 10 characters)
    size = models.CharField(max_length=10)  # Stores size (up to 10 characters)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # Links to a Category model
    material = models.CharField(max_length=100)  # Stores material (up to 100 characters)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, blank=True, null=True)  # Links to a Subcategory model (optional)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True, null=True)  # Links to a Brand model (optional)
    def save(self, *args, **kwargs):
        """Переопределяем метод save для изменения цены с учетом скидки."""
        if self.discount > 0:
            self.price = self.price * (1 - (self.discount / 100))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Photo(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='img')
    photo = models.FileField(upload_to='suratlar', verbose_name='photos')

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photo'


class Photo_2(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='img2')
    photo = models.FileField(upload_to='suratlar', verbose_name='photos')

    class Meta:
        verbose_name = 'photo2'
        verbose_name_plural = 'photo2'


class Photo_3(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='img3')
    photo = models.FileField(upload_to='suratlar', verbose_name='photos')

    class Meta:
        verbose_name = 'photo3'
        verbose_name_plural = 'photo3'