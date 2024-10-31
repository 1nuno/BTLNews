from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(
            username=settings.DJANGO_SUPERUSER_USERNAME
        ).exists():
            User.objects.create_superuser(
                username=settings.DJANGO_SUPERUSER_USERNAME,
                email=settings.DJANGO_SUPERUSER_EMAIL,
                password=settings.DJANGO_SUPERUSER_PASSWORD,
            )
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write("Superuser already exists")
