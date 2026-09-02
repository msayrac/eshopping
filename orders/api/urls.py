
from django.urls import path
from orders.api import api_views
from orders import views


urlpatterns = [
    path('cart/',api_views.CartAPIView.as_view(), name='api-view'),
    path('orders/items/<int:item_id>/',api_views.CartItemRemoveAPIView.as_view(), name='api-cart-item-remove'),
    path('orders/', api_views.OrderListAPIView.as_view(), name='api-order-list'),
]



