from django.shortcuts import render

from store.models import Collection, Product


def say_hello(request):
    collection = Collection(pk=11)
    # collection.delete() (delete single)
    # Collection.objects.filter(id__gt=5).delete() (delete multiple)
    view_context = {'name': 'Nikola'}

    return render(request, 'hello.html', context=view_context)
