from django.shortcuts import render
from django.db import transaction

from store.models import Order, OrderItem


def say_hello(request):
    # non transaction code here...
    with transaction.atomic():
        order = Order(customer_id=1)
        order.save()

        item = OrderItem(order=order, product_id=-1, quantity=1, unit_price=10)
        item.save()
    # non transaction code here...
    view_context = {'name': 'Nikola'}

    return render(request, 'hello.html', context=view_context)
