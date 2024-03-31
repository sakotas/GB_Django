from django.contrib import admin
from django.urls import path, include
from .views import index, from_zero_to_hundred, heads_and_tails, from_one_to_six, show_statistics

urlpatterns = [
    path("", index, name="index"),
    path("from_zero_to_hundred/", from_zero_to_hundred, name="from_zero_to_hundred"),
    path("heads_and_tails/", heads_and_tails, name="heads_and_tails"),
    path("from_one_to_six/", from_one_to_six, name="from_one_to_six"),
    path("heads_and_tails/show_statistics/", show_statistics, name="show_statistics")
]
