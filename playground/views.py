from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # get first object sorted by unit_price from a query_set
    product_from_query_set = Product.objects.order_by('unit_price')[0]
    # gets first object sorted by unit_pricewithout the need of extraction from a query_set
    product = Product.objects.earliest('unit_price')
    view_context = {'name': 'Nikola', 'product': product}

    return render(request, 'hello.html', context=view_context)
