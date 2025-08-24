from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Product, Category
from .serializers import ProductSerializer, UserSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all().order_by('id') # Ordered by ID for consistent pagination
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Configure filters for search, filtering, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Fields to filter on directly
    filterset_fields = {
        'category': ['exact'],
        'price': ['lte', 'gte'], # less than or equal, greater than or equal
        'stock_quantity': ['gt', 'exact'] # greater than, exact
    }

    # Fields to search on
    search_fields = ['name', 'description', 'category__name']

    # Fields to order by
    ordering_fields = ['name', 'price', 'created_date']

class UserCreateView(generics.CreateAPIView):
    """
    An endpoint for user registration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [] # Publicly accessible