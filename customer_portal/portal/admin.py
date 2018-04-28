from django.contrib import admin
from . import models

admin.site.register(models.Shopper)
admin.site.register(models.RegisteredShopper)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.ShoppingCart)
admin.site.register(models.ProductItem)
admin.site.register(models.Coupon)

