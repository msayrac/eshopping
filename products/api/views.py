from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Category, Product
from products.api.serializers import CategorySeriaizer,ProductSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class =CategorySeriaizer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True).select_related('category').order_by('-created_at')
    serializer_class =ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields =['category','category__slug']
    serach_filter=['name','description']
    ordering_fields = ['price','created_at','stock']

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True).select_related('category')
    serializer_class=ProductSerializer


