from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserCreateView, CategoryViewSet

# Create a router instance
router = DefaultRouter()

# Register ViewSets with the router
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    # Router URLs handle all CRUD operations for products and categories
    path('', include(router.urls)),
    # Custom URL for user registration
    path('register/', UserCreateView.as_view(), name='user-register'),
]