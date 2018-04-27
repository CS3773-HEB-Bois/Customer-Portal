from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Product, ProductCategory, ShoppingCart
from ..forms import AddToCartForm

def index(request):
    #cart_id = request.session.get('shopping_cart_id', '')
    #if not cart_id:
    #    return redirect('/')
    shopping_cart = ShoppingCart.objects.get(pk=1)
    product_items = shopping_cart.product_items.all()
    return render(request, 'cart/index.html', {'product_items': product_items})

def add_product(request):
    shopping_cart = ShoppingCart.objects.get(pk=1)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        product = Product.objects.get(pk=form.product_id)
        product_item = shopping_cart.product_items.filter(product==product_id)
        if not product_item:
            product_item = ProductItem()
            product_item.product = product
            product_item.quantity = 0
        product_item.quantity += 1
        shopping_cart.product_items.add(product_item)
    else:
        pass
