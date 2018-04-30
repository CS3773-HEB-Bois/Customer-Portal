from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import ShoppingCart, Order, Coupon, CreditCardInformation, DeliveryPreferences, BillingInformation
from ..forms import DiscountForm, OrderForm


def index(request):
    shopping_cart_id = request.session['shopping_cart_id']
    shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
    shopper = shopping_cart.shopper
    payment_options = CreditCardInformation.objects.filter(shopper=shopper)
    if not shopping_cart.product_items.exists():
        messages.warning(request, 'You don\'t have any items in your cart')
        return redirect('home')

    if not hasattr(shopping_cart, 'order'):
        order = Order()
        order.shopping_cart = shopping_cart
        order.save()
    else:
        order = shopping_cart.order

    if request.method == "GET":
        form = OrderForm()
    elif request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order.save()

            delivery_address = " ".join(
                [
                    form.cleaned_data['delivery_address1'],
                    form.cleaned_data['delivery_address2'],
                    form.cleaned_data['delivery_city'],
                    form.cleaned_data['delivery_state'],
                    form.cleaned_data['delivery_zip'],
                ]
            )
            billing_address = " ".join(
                [
                    form.cleaned_data['billing_address1'],
                    form.cleaned_data['billing_address2'],
                    form.cleaned_data['billing_city'],
                    form.cleaned_data['billing_state'],
                    form.cleaned_data['billing_zip'],
                ]
            )
            delivery_preferences = DeliveryPreferences()
            delivery_preferences.deliveryAddress = delivery_address
            delivery_preferences.deliverySpeed = form.cleaned_data['delivery_option']
            delivery_preferences.order = order
            delivery_preferences.save()
            order.delivery_preferences = delivery_preferences

            billing_information = BillingInformation()
            billing_information.billing_address = billing_address
            billing_information.payment_information_id = form.cleaned_data['payment_option']
            billing_information.order = order
            billing_information.save()
            order.billing_information = billing_information

            shopping_cart.active = False
            shopping_cart.save()
            order.save()
            messages.success(request, 'We have placed your order! Thanks for shopping with us!')
            request.session.pop('shopping_cart_id', None)
            return redirect('home')
        else:
            for field in form:
                print(field)
                print(field.errors)
            messages.warning(
                request, 'Missing necessary information. Please complete all fields and try again')

    context = {
        'form': form,
        'order': order,
        'payment_options': payment_options,
        'shopping_cart': shopping_cart
    }
    return render(request, 'checkout/index.html', context)


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
