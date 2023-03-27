from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    query_set = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type=content_type,
            object_id=1
        )
    view_context = {'name': 'Nikola',
                    'result': list(query_set)}

    return render(request, 'hello.html', context=view_context)
