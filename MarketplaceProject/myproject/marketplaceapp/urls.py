from django.urls import path, include

from .views import index, read_client, create_client, update_client, delete_client

urlpatterns = [
    path("", index, name="index"),
    path("read_client/<int:id>/", read_client, name="read_client_by_id"),
    path("create_client/", create_client, name="create_client"),
    path("update_client/", update_client, name="update_client"),
    path("delete_client/<int:id>/", delete_client, name="delete_client"),
]
