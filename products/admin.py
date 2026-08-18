from django.contrib import admin
from products.models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')

    list_filter = ('name','slug')

    search_fields = ('name','slug')

    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display =('id','category','name','price','stock','is_active','created_at')

    list_filter = ('category','name','price','stock','is_active')

    search_fields = ('category','name','price','stock')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)