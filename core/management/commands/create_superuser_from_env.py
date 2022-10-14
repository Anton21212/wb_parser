import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create project superuser from env'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME')
        superuser = User.objects.filter(username=username).first()
        if superuser and not superuser.is_superuser:
            raise CommandError(f'User with username "{username}" already exists and isn\'t superuser')
        elif not superuser:
            password = os.environ.get('ADMIN_PASSWORD')
            email = ''
            admin = User.objects.create_superuser(
                username=username,
                password=password,
                email=email)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print(f'New superuser "{username}" has been created')
        else:
            print(f'Superuser "{username}" already exists')
