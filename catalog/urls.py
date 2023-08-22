from django.urls import path

from catalog.views import contacts, home, index

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('', index)
]