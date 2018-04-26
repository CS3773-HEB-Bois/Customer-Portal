from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductCategory
import boto3


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)

def product_show(request, product_id):
    product = Product.objects.get( pk=product_id)
    context = {'product': product}
    return render(request, 'products/show.html', context) 


def product_category_show(request, product_category_id):
    cat = ProductCategory.objects.get(pk = product_category_id)
    #cat.products.all()
    context = {'cat': cat}
    return render (request, 'products/showcategory.html',context)