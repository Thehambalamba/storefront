from django.shortcuts import render
from store.models import Order


def say_hello(request):
    # Handling relationships between table with query_sets
    query_set = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    view_context = {'name': 'Nikola', 'orders': query_set}

    return render(request, 'hello.html', context=view_context)
