from django.shortcuts import render
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    query_set_customer = Customer.objects.filter(email__icontains='.com')
    query_set_product = Product.objects.filter(description__isnull=True)
    query_set_product_low_inventory = Product.objects.filter(
        inventory__lt=10)
    query_set_orders_first_customer = Order.objects.filter(
        customer__id=1)
    query_set_order_items_products_collection_3 = OrderItem.objects.filter(
        product__collection__id=3)
    query_set_collection = Collection.objects.filter(
        featured_product__isnull=True)

    view_context = {'name': 'Nikola', 'products': list(
        query_set_product), 'customers': list(query_set_customer), 'collections': list(query_set_collection), 'products_low_inventory': list(query_set_product_low_inventory), 'orders_first_customer': list(query_set_orders_first_customer), 'order_items_products_collection_3': list(query_set_order_items_products_collection_3)}

    return render(request, 'hello.html', context=view_context)
