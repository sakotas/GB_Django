from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'registered_on']
    search_fields = ['name', 'email', 'phone']


admin.site.register(Client, ClientAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'description', 'price', 'quantity', 'date_added']
    list_filter = ['date_added', 'price']
    search_fields = ['item_name']


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_sum', 'date_ordered']
    list_filter = ['date_ordered']
    search_fields = ['client__name', 'client__email']


admin.site.register(Order, OrderAdmin)
