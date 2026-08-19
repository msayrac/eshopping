
from django.urls import path
from products import views
urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]
