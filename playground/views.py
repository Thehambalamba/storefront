from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):
    query_set = Product.objects.filter(id__in=OrderItem.objects.values_list(
        'product_id').distinct()).order_by('title')

    view_context = {'name': 'Nikola', 'query_set': query_set}

    return render(request, 'hello.html', context=view_context)
