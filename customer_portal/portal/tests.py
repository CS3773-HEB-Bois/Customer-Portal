from django.test import TestCase
from customer_portal.portal import models


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = models.Product()
        self.product.price = 485

    def test_calculate_price(self):
        price = self.product.price_in_dollars
        self.assertEqual(price, 4.85)



class RegisteredShopperTestCase(TestCase):
    def setUp(self):
        self.shopper = models.RegisteredShopper()


    def test_has_password(self):
        password = "mypassword"
        self.shopper.set_password(password, password)
        self.assertTrue(self.shopper.has_password(password))


    def test_does_not_have_password(self):
        password = "mypassword"
        self.shopper.set_password(password, "notmypassword")
        self.assertFalse(self.shopper.has_password(password))



class ProductItemTestCase(TestCase):
    def setUp(self):
        self.productItem = models.ProductItem()

    def test_total_in_dollars(self):
        self.product1 = models.Product()
        self.product1.price = 485
        self.product1.save()
        self.productItem.product = self.product1
        self.productItem.quantity = 4
        subtotal = self.productItem.total_in_dollars
        self.assertEqual(subtotal, 19.4)





class ShoppingCartTestCase(TestCase):
    def setUp(self):
        shopper = models.Shopper.objects.create()
        self.shoppingCart = models.ShoppingCart()
        self.shoppingCart.shopper = shopper
        self.shoppingCart.save()


    def test_subtotal_when_empty(self):
        subTotal = self.shoppingCart.subtotal
        self.assertEqual(subTotal, 0)

    def test_subtotal(self):
        self.product1 = models.Product()
        self.product1.price = 485
        self.product1.save()

        self.productItem1 = models.ProductItem()
        self.productItem1.product = self.product1
        self.productItem1.quantity = 3
        self.shoppingCart.product_items.add(self.productItem1, bulk=False)

        self.product2 = models.Product()
        self.product2.price = 895
        self.product2.save()


        self.productItem2 = models.ProductItem()
        self.productItem2.product = self.product2
        self.productItem2.quantity =1
        self.shoppingCart.product_items.add(self.productItem2, bulk=False)

        self.product3 = models.Product()
        self.product3.price = 1175
        self.product3.save()


        self.productItem3 = models.ProductItem()
        self.productItem3.product = self.product3
        self.productItem3.quantity = 2
        self.shoppingCart.product_items.add(self.productItem3, bulk=False)

        subTotal = self.shoppingCart.subtotal
        self.assertEqual(subTotal, 47.0)


class OrderTestCase(TestCase):
    def setUp(self):
        shopper = models.Shopper.objects.create()
        self.shoppingCart = models.ShoppingCart()
        self.shoppingCart.shopper = shopper
        self.shoppingCart.save()
        self.order = models.Order()
        self.order.shopping_cart = self.shoppingCart
        self.order.save()


    def test_tax(self):
        self.product1 = models.Product()
        self.product1.price = 100
        self.product1.save()

        self.productItem1 = models.ProductItem()
        self.productItem1.product = self.product1
        self.productItem1.quantity = 1
        self.shoppingCart.product_items.add(self.productItem1, bulk=False)

        tax = self.order.tax
        self.assertEqual(tax, 0.0825)


    def test_total_discount(self):
        discount1 = models.Discount()
        discount1.amount = 500
        discount1.save()
        self.order.discounts.add(discount1)

        discount2 = models.Discount()
        discount2.amount = 100
        discount2.save()
        self.order.discounts.add(discount2)

        discountTotal = self.order.total_discount
        self.assertEqual(discountTotal, 6.0)


    def test_total(self):
        self.product1 = models.Product()
        self.product1.price = 100
        self.product1.save()

        self.productItem1 = models.ProductItem()
        self.productItem1.product = self.product1
        self.productItem1.quantity = 1
        self.shoppingCart.product_items.add(self.productItem1, bulk=False)

        total = self.order.total
        self.assertEqual(total, 1.0825)



