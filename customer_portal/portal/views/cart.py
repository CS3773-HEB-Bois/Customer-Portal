from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Product, ProductCategory, ShoppingCart, ProductItem
from ..forms import AddToCartForm


def index(request):
    cart_id = request.session['shopping_cart_id']
    if cart_id:
        shopping_cart = ShoppingCart.objects.get(pk=cart_id)
        if shopping_cart:
            product_items = shopping_cart.product_items.all()
            context = {
                'product_items': product_items,
                'cart': shopping_cart
            }
            return render(request, 'cart/index.html', context)
    return redirect('/')


def add_product(request):
    shopping_cart_id = request.session['shopping_cart_id']
    shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            product_item = shopping_cart.product_items.filter(
                product=product_id).first()
            if not product_item:
                product_item = ProductItem()
                product_item.product_id = product_id
                product_item.quantity = 0
            product_item.quantity += 1
            shopping_cart.product_items.add(product_item, bulk=False)
            shopping_cart.save()
    return redirect('/')
