from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from products.models import Product
from orders.models import Cart, CartItem,Order
from orders.api.serializers import CartSerializer,CartItemSerializer


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity =int(request.data.get('quantity',1))

        if not product_id:
            return Response({'error': 'yetersiz stok.'}, status =status.HTTP_400_BAD_REQUEST)
        
        product = get_object_or_404(Product, id=product_id)

        if product.stock < quantity:
            return Response({'error':'Yetersiz stok'}, status=status.HTTP_400_BAD_REQUEST)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        serializer =CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartItemRemoveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request, item_id):
        cart =get_object_or_404(Cart,user=request.user)
        cart_item = get_object_or_404(CartItem,id=item_id,cart=cart)
        cart_item.delete()
        return Response({'message':'Ürün Sepetten Kaldırıldı.'}, status=status.HTTP_204_NO_CONTENT)

class OrderListAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        searializer =CartSerializer(orders, many=True)
        return Response(searializer.data, status=status.HTTP_200_OK)






