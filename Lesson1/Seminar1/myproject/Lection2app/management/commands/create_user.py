from django.core.management.base import BaseCommand

from Lection2app.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Neo', email='john@example.com', password='secret', age=25)
        user = User(name='Jack', email='john@example.com', password='secret', age=25)
        user.save()
        self.stdout.write(f'{user}')
