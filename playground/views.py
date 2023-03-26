from django.shortcuts import render
from django.db.models.aggregates import Count, Min
from store.models import Product


def say_hello(request):
    result = Product.objects.aggregate(
        count=Count('id'), min_price=Min('unit_price'))

    view_context = {'name': 'Nikola', 'result': result}

    return render(request, 'hello.html', context=view_context)
