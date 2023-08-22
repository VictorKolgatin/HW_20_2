from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list':product_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
