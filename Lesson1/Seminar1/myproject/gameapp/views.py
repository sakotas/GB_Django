import random
import logging
from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from django.http import HttpResponse

# from .models import Coin

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Page accessed")
    return HttpResponse("Hello World!")


def heads_and_tails(request):
    result = random.choice(['Heads!', 'Tails!'])
    coin = Coin(side=result, time=timezone.now())
    coin.save()
    return HttpResponse(result)


def show_statistics(request):
    values = list(Coin.get_statistics())
    result_list = []
    for value in values:
        result_list.append(value.side)
    return HttpResponse(f'Statistics:\n'
                        f'{result_list}')


def from_one_to_six(request):
    return HttpResponse(f"Random number: {random.randint(1, 6)}")


def from_zero_to_hundred(request):
    return HttpResponse(f"Random number: {random.randint(0, 100)}")
