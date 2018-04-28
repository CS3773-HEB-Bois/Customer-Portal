from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import ShoppingCart, Order, Coupon
from ..forms import DiscountForm


def index(request):
    shopping_cart_id = request.session['shopping_cart_id']
    shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
    if not shopping_cart.product_items:
        messages.warning(request, 'You don\'t have any items in your cart')
        return redirect('home')
    if request.method == "GET":
        form = DiscountForm()
        context = {
            'form': form,
            'shopping_cart': shopping_cart
        }
        return render(request, 'checkout/index.html', context)
    elif request.method == "POST":
        if not shopping_cart.order:
            order = Order()
            shopping_cart.order = Order()

        context = {
            'shopping_cart': shopping_cart
        }
    return redirect('home')


def add_discount(request):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        code = form.data['code']
        # Check if the coupon code exists
        coupon = Coupon.objects.filter(code=code).first()
        if coupon:
            shopping_cart_id = request.session['shopping_cart_id']
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if not hasattr(shopping_cart, 'order'):
                order = Order()
                order.shopping_cart = shopping_cart
                order.save()
            else:
                order = shopping_cart.order
            if not order.discounts.filter(coupon__code=code).exists():
                order.discounts.add(coupon)
                order.save()
                messages.success(request, 'Discount %s applied!' % code)
            else:
                messages.warning(
                    request, 'Discount %s has already been applied' % code)

        else:
            messages.warning(request, 'Discount %s does not exist' % code)
    return redirect('checkout')
