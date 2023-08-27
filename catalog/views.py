from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.

def index(request):
    product_list = Category.objects.all()
    context = {
        'object_list':product_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')

def products(request, pk):
    category_name = Category.objects.get(pk=pk)
    data = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Каталог товаров - {category_name.name}'
    }
    return render(request, 'catalog/products.html', data)

def article(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'product': product,
        'title': f'Каталог товаров - {product.name}'
    }
    return render(request, 'catalog/article.html', data)

