from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router instance
router = DefaultRouter()

# Register the ProductViewSet with the router
# The first argument is the URL prefix ('products' in this case)
# The second argument is the ViewSet class
# The basename is used to name the URLs for reverse lookups
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]