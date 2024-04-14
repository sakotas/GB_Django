from django.http import HttpResponse
from .models import Client
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect
from .forms import ProductForm


def index(request):
    return render(request, "base.html")


def create_client(request):
    result_list = []
    for i in range(0, 10):
        client = Client(
            name=f"Client{i}",
            email=f"email{i}",
            phone="+7" + str(i),
            address=f"123 456 7890{i}",
        )
        client.save()
        result_list.append(client.name)
    return HttpResponse(f"Clients {result_list} is created!")


def read_client(request, id):
    client = Client.objects.get(id=id)
    return HttpResponse(f"You've requested Client with id: {client.name}")


def update_client(request):
    for client in Client.objects.all():
        client.name = client.name + "1"
        client.save()
    return HttpResponse("Client updated")


def delete_client(request, id):
    client = Client.objects.get(id=id)
    if client is not None:
        client.delete()
    return HttpResponse(f"Client {client.name} deleted")


def get_products(client_id, days):
    date_threshold = timezone.now() - timedelta(days=days)
    client = get_object_or_404(Client, id=client_id)
    orders = Order.objects.filter(client=client, date_ordered__gte=date_threshold)
    products = set()
    for order in orders:
        for product in order.products.all():
            products.add(product)
    return products


def order_by_date(request, client_id=1):
    context = {
        "client_id": client_id,
        "products_last_week": get_products(client_id, 7),
        "products_last_month": get_products(client_id, 30),
        "products_last_year": get_products(client_id, 365),
    }
    return render(request, "orders/order_by_date.html", context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Предполагаем, что есть такой URL
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

