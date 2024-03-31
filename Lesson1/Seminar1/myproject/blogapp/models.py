from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.birthday}'


@receiver(pre_save, sender=Author)
def set_full_name(sender, instance, **kwargs):
    instance.full_name = f'{instance.first_name} {instance.last_name}'
