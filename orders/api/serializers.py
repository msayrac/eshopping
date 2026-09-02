from rest_framework import serializers
from orders.models import Cart, CartItem
from products.api.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
   product = ProductSerializer(read_only=True)
   # product_id = serializers.IntegerField(write_only=True)
   # total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

   class Meta:
      model = CartItem
      fields = ['id','product','price','quantity','total_price']



class CartSerializer(serializers.ModelSerializer):
   items = CartItemSerializer(many=True, read_only=True)
   # total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

   class Meta:
      model = Cart
      fields = ['id', 'status', 'address', 'total_price', 'created_at', 'items']




















