from django.shortcuts import render

from store.models import Collection, Product


def say_hello(request):
    Collection.objects.filter(pk=11).update(featured_product=None)

    view_context = {'name': 'Nikola'}

    return render(request, 'hello.html', context=view_context)
