from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListView, CustomerProductListView

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product-list', ProductListView)
router.register(r'customer-product-list', CustomerProductListView)
urlpatterns = [
  
] + router.urls