from django.shortcuts import render

from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()
    # if we evaluate all objects in a query_set reading from the same query set after will come from cache
    list(query_set)
    query_set[0]
    view_context = {'name': 'Nikola',
                    'result': list(query_set)}

    return render(request, 'hello.html', context=view_context)
