from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField
from store.models import Product


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField())
    query_set = Product.objects.annotate(
        discounted_price=discounted_price)
    view_context = {'name': 'Nikola',
                    'result': query_set}

    return render(request, 'hello.html', context=view_context)
