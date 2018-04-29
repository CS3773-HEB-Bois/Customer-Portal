from django.shortcuts import render
from django.http import HttpResponse
from ..models import Product, ProductCategory
from ..forms import AddToCartForm


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)


def show(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'products/show.html', context)


def product_categories(request):
    categories = ProductCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'products/categories/index.html', context)


def product_category_show(request, product_category_slug):
    cat = ProductCategory.objects.filter(slug=product_category_slug).first()
    if cat:
        cat.products.all()
        context = {'cat': cat}
        return render(request, 'products/categories/show.html', context)
    return redirect('home')
