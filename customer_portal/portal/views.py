from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, ShoppingCart
import boto3


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)

def cart_index(request):
    #cart_id = request.session.get('shopping_cart_id', '')
    #if not cart_id:
    #    return redirect('/')
    shopping_cart = ShoppingCart.objects.get(pk=1)
    product_items = shopping_cart.product_items.all()


    return render(request, 'cart/index.html', {'product_items': product_items})


