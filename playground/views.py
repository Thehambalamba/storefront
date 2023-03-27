from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    query_set = TaggedItem.objects.get_tags_for(
        object_type=Product, object_id=1)
    view_context = {'name': 'Nikola',
                    'result': list(query_set)}

    return render(request, 'hello.html', context=view_context)
