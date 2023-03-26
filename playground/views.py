from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Min, Max
from store.models import Order, OrderItem, Product


def say_hello(request):
    number_of_orders = Order.objects.aggregate(number_of_orders=Count('id'))
    number_of_product_1_sold = OrderItem.objects.filter(
        product__id=1).aggregate(number_of_product_1_sold=Sum('quantity'))
    number_of_orders_for_customer_1 = Order.objects.filter(
        customer_id=1).aggregate(number_of_orders_for_customer_1=Count('id'))
    price_stats_for_products_from_collection_3 = Product.objects.filter(
        collection__id=3).aggregate(min_price=Min('unit_price'), avg_price=Avg('unit_price'), max_price=Max('unit_price'))
    result = {**number_of_orders, **number_of_product_1_sold,
              **number_of_orders_for_customer_1, "price_stats_for_products_from_collection_3": price_stats_for_products_from_collection_3}
    view_context = {'name': 'Nikola',
                    'result': result}

    return render(request, 'hello.html', context=view_context)
