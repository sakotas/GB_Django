from django.http import HttpResponse
from .models import Client


# Create your views here.
def index(request):
    return HttpResponse("Welcome to Marketplace App")


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
