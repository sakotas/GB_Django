from django.db import models
from django.http import HttpResponse
from django.utils import timezone


# Create your models here.
# class Coin(models.Model):
#     side = models.CharField(max_length=100)
#     time = models.DateTimeField(default=timezone.now())
#
#     def __str__(self):
#         return f'Side: {self.side} Time: {self.time}'
#
#     @staticmethod
#     def get_statistics():
#         values = Coin.objects.order_by('-time')[:5]
#         return values
