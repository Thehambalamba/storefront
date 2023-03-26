from django.shortcuts import render
from django.db.models import F
from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(inventory=F('collection__id'))
    view_context = {'name': 'Nikola', 'query_set': list(query_set)}

    return render(request, 'hello.html', context=view_context)
