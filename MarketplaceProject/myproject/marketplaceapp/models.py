from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.item_name} - {self.description} - {self.price}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Product, related_name="orders")
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.client.name} on {self.date_ordered.strftime("%Y-%m-%d")}'

    def update_total_sum(self):
        self.total_sum = sum(
            product.price * product.quantity for product in self.products.all()
        )
        self.save()
