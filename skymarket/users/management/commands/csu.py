from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='admin',
            last_name='admin',
            role='admin',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('0000')
        user.save()
        print('Admin user created.')