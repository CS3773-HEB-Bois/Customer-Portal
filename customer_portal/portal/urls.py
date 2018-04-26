from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>', views.product_show, name='alan'),
    path('products/category/<int:product_category_id>', views.product_category_show,name='cat'),
    path('products/category/all', views.category_show,name='category_all'),

]
