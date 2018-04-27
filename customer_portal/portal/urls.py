from django.urls import path

from . import views

urlpatterns = [
    path('', views.products.index, name='index'),
    path('products/<int:product_id>', views.products.show, name='products_show'),
    path('cart', views.cart.index, name='cart'),
    path('categories', views.products.product_categories,name='category_all'),
    path('categories/<int:product_category_id>', views.products.product_category_show,name='cat'),
]
