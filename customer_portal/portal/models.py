from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.hashers import check_password, make_password


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

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
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255)

    def set_password(self, password, password_confirmation):
        if password == password_confirmation:
            self.password_hash = make_password(password)
            return True
        return False

    def has_password(self, password):
        return check_password(password, self.password_hash)

    def __str__(self):
        return self.first_name + " " + self.last_name


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
    code = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.code


class ShoppingCart(models.Model):
    shopper = models.ForeignKey(
        Shopper, related_name="shopping_carts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    ordering = ['created_at']

    @property
    def subtotal(self):
        subtotal = sum(p.product.price *
                       p.quantity for p in self.product_items.all())
        return subtotal / 100


class ProductItem(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(
        ShoppingCart, related_name='product_items', on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.product.name, self.quantity)
    
    @property
    def total_in_dollars(self):
        return (self.product.price * self.quantity)/100


class Order(models.Model):
    delivery_fee = models.IntegerField(default=0)
    shopping_cart = models.OneToOneField(
        ShoppingCart, on_delete=models.CASCADE)
    billing_information = models.ForeignKey(
        BillingInformation, on_delete=models.SET_NULL, null=True)
    delivery_preferences = models.ForeignKey(
        DeliveryPreferences, on_delete=models.SET_NULL, null=True)
    discounts = models.ManyToManyField(Discount)
