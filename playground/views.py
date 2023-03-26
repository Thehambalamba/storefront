from django.shortcuts import render
from django.db.models import Value, F
from store.models import Customer


def say_hello(request):
    # add fields to a table using annotate
    query_set = Customer.objects.annotate(
        new_id=F('id') + 1, is_new=Value(True))
    view_context = {'name': 'Nikola',
                    'result': query_set}

    return render(request, 'hello.html', context=view_context)
