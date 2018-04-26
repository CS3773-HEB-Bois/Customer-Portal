from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, ProductCategory, ShoppingCart
import boto3


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)


def product_show(request, product_id):
    product = Product.objects.get( pk=product_id)
    context = {'product': product}
    return render(request, 'products/show.html', context) 


def product_category_show(request, product_category_id):
    cat = ProductCategory.objects.get(pk = product_category_id)
    #cat.products.all()
    context = {'cat': cat}
    return render (request, 'products/showcategory.html',context)

def cart_index(request):
    #cart_id = request.session.get('shopping_cart_id', '')
    #if not cart_id:
    #    return redirect('/')
    shopping_cart = ShoppingCart.objects.get(pk=1)
    product_items = shopping_cart.product_items.all()


    return render(request, 'cart/index.html', {'product_items': product_items})

