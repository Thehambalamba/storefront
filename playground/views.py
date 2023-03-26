from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # We can deferr fields from being loaded (but we need to make sure we dont call this deferred field else where as it will result in a bunch of unecesary queries).
    query_set = Product.objects.defer('description')

    view_context = {'name': 'Nikola', 'query_set': query_set}

    return render(request, 'hello.html', context=view_context)
