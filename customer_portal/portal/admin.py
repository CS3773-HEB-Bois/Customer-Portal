from django.contrib import admin
from . import models

admin.site.register(models.Shopper)
admin.site.register(models.RegisteredShopper)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
