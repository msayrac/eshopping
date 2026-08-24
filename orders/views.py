from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from orders.models import Cart, CartItem

# Create your views here.

# @login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'orders/cart_detail.html', {'cart':cart})

# @login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart, created = Cart.objects.get_or_create(user = request.user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart_item.quantity =1
        cart_item.save()

# @login_required
def decrease_cart_item(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)


    if cart_item.quantity >1:
        cart_item -=1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_detail')

# @login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user =request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem,cart =cart, product = product)

    cart_item.delete()
    return redirect('cart-detail')


