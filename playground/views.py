from django.shortcuts import render
from django.db.models import Count
from store.models import Customer


def say_hello(request):
    query_set = Customer.objects.annotate(orders_count=Count('order'))
    view_context = {'name': 'Nikola',
                    'result': query_set}

    return render(request, 'hello.html', context=view_context)
