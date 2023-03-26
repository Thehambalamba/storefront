from django.shortcuts import render
from django.db.models import Value
from django.db.models.functions import Concat
from store.models import Customer


def say_hello(request):
    # anotate concated filds
    query_set = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    )
    view_context = {'name': 'Nikola',
                    'result': query_set}

    return render(request, 'hello.html', context=view_context)
