
from django.urls import path
from orders import views
urlpatterns = [
    path('cart/', views.cart_detail, name='cart-detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/decrease/<int:product_id>/', views.decrease_cart_item, name='decrease-cart-item'),
    path('cart/removo/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.order_list, name='order-list'),
    path('my-orders/<int:order_id>/', views.order_detail, name='order-detail'),
   
]
