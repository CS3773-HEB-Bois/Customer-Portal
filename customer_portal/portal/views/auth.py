from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from ..models import RegisteredShopper, ShoppingCart
from ..forms import LoginForm, RegistrationForm


def login(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = {
            'form': login_form
        }
        return render(request, 'auth/login.html', context)
    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            shopper = RegisteredShopper.objects.filter(
                username=username).first()
            if shopper:
                if shopper.has_password(password):
                    carts = shopper.shopping_carts.filter(
                        active=True).order_by('-created_at')
                    if not carts:
                        shopping_cart = ShoppingCart()
                        shopping_cart.save()
                        shopper.shopping_carts.add(shopping_cart, Bulk=False)
                    else:
                        shopping_cart = carts.first()
                    shopper.save()
                    request.session['shopper_id'] = shopper.id
                    request.session['shopping_cart_id'] = shopping_cart.id
                    return redirect('/')
        context = {'form': login_form}
        return render(request, 'auth/login.html', context)


def logout(request):
    if request.method == "GET":
        if 'shopper_id' in request.session:
            request.session.pop('shopper_id', None)
        if 'shopping_cart_id' in request.session:
            request.session.pop('shopping_cart_id', None)
    return redirect('/')


def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'auth/register.html', context)
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            shopper = form.save(commit=False)
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            if shopper.set_password(password, password_confirmation):
                shopper.save()
                shopping_cart = ShoppingCart()
                shopping_cart.shopper = shopper
                shopping_cart.save()
                request.session['shopper_id'] = shopper.id
                request.session['shopping_cart_id'] = shopping_cart.id
    return redirect('/')
