from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product categories"


class Product(models.Model):
    available_stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, related_name="products", null=True)

    @property
    def price_in_dollars(self):
        return self.price/100

    def __str__(self):
        return self.name


class Shopper(models.Model):
    pass


class RegisteredShopper(Shopper):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)


class ShoppingCart(models.Model):
    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)


class ProductItem(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(
        ShoppingCart, related_name='product_items', on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}: {}".format(self.product.name, self.quantity)


class PaymentInformation(models.Model):
    pass


class BillingInformation(models.Model):
    billing_address = models.CharField(max_length=255)
    payment_information = models.ForeignKey(
        PaymentInformation, on_delete=models.CASCADE)


class DeliveryPreferences(models.Model):
    deliveryAddress = models.CharField(max_length=255)


class Discount(models.Model):
    amount = models.IntegerField(default=0)


class Coupon(Discount):
    code = models.CharField(max_length=128)


class Order(models.Model):
    subtotal = models.IntegerField(default=0)
    delivery_fee = models.IntegerField(default=0)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    billing_information = models.ForeignKey(
        BillingInformation, on_delete=models.SET_NULL, null=True)
    delivery_preferences = models.ForeignKey(
        DeliveryPreferences, on_delete=models.SET_NULL, null=True)
    discount = models.ManyToManyField(Discount)
