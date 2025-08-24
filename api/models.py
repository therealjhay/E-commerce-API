from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    A model to categorize products.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    A model representing a product in the e-commerce store.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # The ForeignKey links a product to a category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    stock_quantity = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name