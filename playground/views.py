from django.shortcuts import render

from store.models import Collection, Product


def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()

    view_context = {'name': 'Nikola'}

    return render(request, 'hello.html', context=view_context)
