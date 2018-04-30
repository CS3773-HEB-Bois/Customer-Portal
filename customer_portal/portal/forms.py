from django import forms
from .models import Product, RegisteredShopper, Coupon, CreditCardInformation


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


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code']


class AddCreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCardInformation
        fields = ['card_number', 'cvv', 'month', 'year']


class OrderForm(forms.Form):
    billing_address1 = forms.CharField(max_length=255, min_length=4)
    billing_address2 = forms.CharField(
        max_length=255, min_length=4, required=False)
    billing_city = forms.CharField(max_length=255, min_length=4)
    billing_state = forms.CharField(max_length=255, min_length=2)
    billing_zip = forms.CharField(max_length=255, min_length=4)
    payment_option = forms.IntegerField()

    delivery_address1 = forms.CharField(max_length=255, min_length=4)
    delivery_address2 = forms.CharField(
        max_length=255, min_length=4, required=False)
    delivery_city = forms.CharField(max_length=255, min_length=4)
    delivery_state = forms.CharField(max_length=255, min_length=2)
    delivery_zip = forms.CharField(max_length=255, min_length=4)
    delivery_option = forms.CharField(max_length=255, min_length=4)
