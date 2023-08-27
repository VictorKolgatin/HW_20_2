from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, index, products, article

app_name = CatalogConfig.name
urlpatterns = [
    # path('', home),
    path('contacts/', contacts),
    path('', index),
    path('products/<int:pk>/', products, name='products'),
    path('article/<int:pk>/', article, name='article'),
]