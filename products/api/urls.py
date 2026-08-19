from django.urls import path
from products.api.views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView

urlpatterns = [
    path('products/',ProductListAPIView.as_view(), name='api-product-list'),
    path('products/<int:pk>/',ProductDetailAPIView.as_view(), name='api-product-detail'),
    path('categories/',CategoryListAPIView.as_view(), name='api-category-list'),
]
