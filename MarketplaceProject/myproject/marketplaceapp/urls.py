from django.urls import path, include

from .views import (
    index,
    read_client,
    create_client,
    update_client,
    delete_client,
    order_by_date,
)

urlpatterns = [
    path("", index, name="index"),
    path("read_client/<int:id>/", read_client, name="read_client_by_id"),
    path("create_client/", create_client, name="create_client"),
    path("update_client/", update_client, name="update_client"),
    path("delete_client/<int:id>/", delete_client, name="delete_client"),
    path("order_by_date/", order_by_date, name="order_by_date-default"),
    path("order_by_date/<int:client_id>/", order_by_date, name="order_by_date"),
]
