from django.contrib import admin
from django.urls import path, include
from .views import index, create_random_authors

urlpatterns = [
    path("", index, name="index"),
    path("create_random_authors/", create_random_authors, name="create_random_authors")
]
