from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)
    
    def __str__(self):
            return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    manufacturer = models.ManyToManyField("Manufacturer", related_name="products")
    size = models.IntegerField(default=0)
    date_added = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    in_catalog = models.BooleanField(default=False, verbose_name="Show in catalog?")

    def __str__(self):
        return "{} ({})".format(self.title, self.category.name)

class Manufacturer(models.Model):
    name = models.CharField(max_length=70, help_text="Use short name if possible", unique=True)

    def __str__(self):
        return self.name