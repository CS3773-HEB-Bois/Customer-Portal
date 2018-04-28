from django import forms
from .models import Product, RegisteredShopper


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=4)
    password = forms.CharField(max_length=255, min_length=6)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=128, min_length=6)
    password_confirmation = forms.CharField(max_length=128, min_length=6)

    class Meta:
        model = RegisteredShopper
        fields = ['email', 'username', 'first_name', 'last_name']

