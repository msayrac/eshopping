from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Sepet"

    @property
    def total_price(self):
        # Sepetteli ürünlerin toplam fiyatı
        item_total_price=0
        items = Product.objects.all()
        for item in items:
            item_total_price += item.price
        return item_total_price

    @property
    def total_items_count(self):
        # sepetteki toplam ürün sayısıs
        return sum(item.quantity for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together =('cart','product')

    def __str__(self):
        return f"{self.product.name}  ({self.quantity} adet)"

    @property
    def total_price_individual_item(self):
        # Tek bir ürün fiyatı priceXquantity
        return self.product.price*self.quantity