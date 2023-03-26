from django.shortcuts import render
from django.db.models import Q
from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(
        Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    view_context = {'name': 'Nikola', 'query_set': list(query_set)}

    return render(request, 'hello.html', context=view_context)
