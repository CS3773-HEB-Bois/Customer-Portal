from django.urls import path

from . import views

urlpatterns = [
    path('', views.products.index, name='home'),
    path('products/<int:product_id>', views.products.show, name='view_product'),

    path('cart', views.cart.index, name='cart'),
    path('cart/add', views.cart.add_product, name='add_to_cart'),

    path('checkout', views.checkout.index, name='checkout'),
    path('checkout/discount', views.checkout.add_discount, name='add_discount'),

    path('categories', views.products.product_categories, name='categories'),
    path('categories/<int:product_category_id>',
         views.products.product_category_show, name='view_category'),

    path('login', views.auth.login, name="login"),
    path('logout', views.auth.logout, name="logout"),
    path('register', views.auth.register, name="register")
]
