from django import forms
from .models import Product


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=4)
    password = forms.CharField(max_length=255, min_length=6)
