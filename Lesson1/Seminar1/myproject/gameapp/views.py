import random
import logging
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page accessed')
    return HttpResponse('Hello World!')


def heads_and_tails(request):
    if random.randint(0, 1):
        logger.info(f'Result 1')
        return HttpResponse('Heads!')
    logger.info(f'Result 0')
    return HttpResponse('Tails!')


def from_one_to_six(request):
    return HttpResponse(f'Random number: {random.randint(1, 6)}')


def from_zero_to_hundred(request):
    return HttpResponse(f'Random number: {random.randint(0, 100)}')
