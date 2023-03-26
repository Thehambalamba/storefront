from django.shortcuts import render
from django.db.models import Max, Count, Sum, F
from store.models import Customer, Collection, Product


def say_hello(request):
    customers_last_order_id = Customer.objects.annotate(
        last_order_id=Max('order__id')).values()
    collections_count_of_products = Collection.objects.annotate(
        count_of_products=Count('product__id')).values()
    customers_more_than_five_orders = Customer.objects.annotate(
        orders_count=Count('order')).filter(orders_count__gt=5).values
    customers_total_amount_spent = Customer.objects.annotate(
        amount_spent_total=Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity'))).values()
    products_top_five_sellers_total_sales = Product.objects.annotate(
        total_sales=Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-total_sales')[:5].values()
    view_context = {'name': 'Nikola',
                    'result': products_top_five_sellers_total_sales}

    return render(request, 'hello.html', context=view_context)
