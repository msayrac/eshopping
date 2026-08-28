from django.contrib import admin
from orders.models import Cart, CartItem, Order, OrderItem

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display =('id','user')


class CardItemAdmin(admin.ModelAdmin):
    list_display =('id','cart','product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','first_name','status','total_price')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','order','product','price','quantity')

admin.site.register(Cart,CardAdmin)
admin.site.register(CartItem,CardItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)