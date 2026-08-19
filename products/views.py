from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
# Create your views here.


def product_list(request):
    products = Product.objects.all()

    context = {
        'products':products
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product':product
    }
    return render(request, 'products/product_detail.html', context)