from django.contrib import admin
from orders.models import Cart, CartItem

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display =('id','user')


class CardItemAdmin(admin.ModelAdmin):
    list_display =('id','cart','product')


admin.site.register(Cart,CardAdmin)
admin.site.register(CartItem,CardItemAdmin)