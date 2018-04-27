from django.shortcuts import render, redirect
from ..models import RegisteredShopper
from ..forms import LoginForm


def login(request):
    if request.method == "GET":
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'auth/login.html', context)
    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print("HERE")
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            shopper = RegisteredShopper.objects.filter(
                username=username).first()
            if shopper:
                # validate password
                request.session['shopper_id'] = shopper.id
                # find shopping_cart
                shopping_cart = ShoppingCart()
                shopping_cart.save()
                shopper.shopping_cart = shopping_cart
                shopper.save()
                request.session['shopping_cart_id'] = shopping_cart.id
    return redirect('/')


def logout(request):
    if request.method == "POST":
        if 'shopper_id' in request.session:
            del request.session['shoppper_id']
        if 'shopping_cart_id' in request.session:
            del request.session['shopping_cart_id']
    return redirect('/')


def register(request):
    pass
