from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # select_related (one to one)
    query_set_select_related = Product.objects.select_related(
        'collection').all()
    # prefetch_related (many to many)
    query_set_prefetch_related = Product.objects.prefetch_related(
        'promotions').all()
    # combined
    query_set = Product.objects.prefetch_related(
        'promotions').select_related('collection').all()

    view_context = {'name': 'Nikola', 'query_set': query_set}

    return render(request, 'hello.html', context=view_context)
