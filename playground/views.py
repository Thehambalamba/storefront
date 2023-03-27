from django.shortcuts import render
from django.db import connection
from store.models import Product


def say_hello(request):
    # using raw
    query_set = Product.objects.raw('SELECT id, title FROM store_product')

    # using connection.cursor
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, title FROM store_product')

    view_context = {'name': 'Nikola', "result": list(query_set)}

    return render(request, 'hello.html', context=view_context)
