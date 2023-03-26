from django.shortcuts import render
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()[5:10]
    view_context = {'name': 'Nikola', 'query_set': query_set}

    return render(request, 'hello.html', context=view_context)
