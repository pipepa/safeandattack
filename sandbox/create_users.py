from django.core.management.base import BaseCommand
from .models import VulnerableUser
from faker import Faker

class Command(BaseCommand):
    help = 'Створити 100 тестових користувачів у пісочниці'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = [
            VulnerableUser(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(length=8)
            )
            for _ in range(100)
        ]
        VulnerableUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Успішно створено 100 користувачів'))
