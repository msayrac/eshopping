from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from products.models import Product
from orders.models import Cart, CartItem, Order, OrderItem

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
    return redirect('cart-detail')
 
# @login_required
def decrease_cart_item(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    if cart_item.quantity >1:
        cart_item.quantity = cart_item.quantity - 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart-detail')

# @login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user =request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem,cart =cart, product = product)

    cart_item.delete()
    return redirect('cart-detail')


# @login_required
def checkout(request):
    cart = get_object_or_404(Cart, user = request.user)

    if not cart.items.exists():
        messages.warning(request, 'The chart is empty so that we cannot procced to payment... Please add an item to the basket')
        return redirect('product-list')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        # available stoks
        for item in cart.items.all():
            if item.quantity > item.product.stock:
                messages.error(request, f"{item.product.name} does not have enoug stock!")
                return redirect('cart-detail')

        # Atomik Sipariş Oluşturma
        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
                total_price=cart.total_price,
                status='completed'
            )

            for item in cart.items.all():
                # Sipariş satırı oluştur
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
                # Stok düş
                item.product.stock -= item.quantity
                item.product.save()

            # Sepeti temizle
            cart.items.all().delete()

        return render(request, 'orders/order_success.html', {'order': order})

    return render(request, 'orders/checkout.html', {'cart': cart})












