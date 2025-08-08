from django.shortcuts import render

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer