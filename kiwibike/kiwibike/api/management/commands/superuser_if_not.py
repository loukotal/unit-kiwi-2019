import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates superuser from SUPERUSER_USERNAME and SUPERUSER_PASSWORD env'

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.environ['SUPERUSER_EMAIL']
        password = os.environ['SUPERUSER_PASSWORD']
        username = os.environ["SUPERUSER_USERNAME"]

        if User.objects.filter(email=email).exists():
            self.stdout.write('Superuser already exists!')

        else:
            User.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
