from rest_framework import serializers
from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    product_count = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        model =Category
        fields = ['id','name', 'slug','product_count']

class ProductSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','is_active','category','category_detail','created_at']












