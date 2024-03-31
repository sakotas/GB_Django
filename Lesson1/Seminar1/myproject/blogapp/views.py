from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Author


# Create your views here.
def index(request):
    return HttpResponse("Blog App!")


def create_random_authors(request):
    result_list = []
    for i in range(0, 10):
        author = Author(first_name=f'Name{i}',
                        last_name=f'Surname{i}',
                        email=f'email{i}@ya.ru',
                        bio=f'bla{i} bla{i} bla{i}...',
                        birthday=timezone.now())
        author.save()
        result_list.append(author.full_name)
    return HttpResponse(f"Added following to db: \n"
                        f"{result_list}")
