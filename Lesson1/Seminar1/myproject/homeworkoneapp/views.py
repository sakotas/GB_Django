import logging
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <nav>
            <ul>
                <li><a href="/homework/">Главная</a></li>
                <li><a href="/homework/about/">О себе</a></li>
            </ul>
        </nav>
        <p>Это главная страница моего первого сайта на Django. Здесь будет располагаться информация о сайте.</p>
    </body>
    </html>
    """
    logger.info("Index: Page accessed")
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>О себе</title>
    </head>
    <body>
        <h1>Информация обо мне</h1>
        <nav>
            <ul>
                <li><a href="/homework/">Главная</a></li>
                <li><a href="/homework/about/">О себе</a></li>
            </ul>
        </nav>
        <p>Здесь я расскажу немного о себе...</p>
    </body>
    </html>
    """
    logger.info("About: Page accessed")
    return HttpResponse(html)
