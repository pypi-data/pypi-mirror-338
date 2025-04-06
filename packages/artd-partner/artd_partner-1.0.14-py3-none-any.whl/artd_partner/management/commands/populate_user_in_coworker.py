from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()
from artd_partner.models import Partner, Coworker


class Command(BaseCommand):
    help = "Populate user in coworker"

    def handle(self, *args, **kwargs):
        for coworker in Coworker.objects.all():
            user = User.objects.filter(email=coworker.email).first()
            if user:
                coworker.user = user
                coworker.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"User {user.email} added to coworker {coworker.first_name} {coworker.last_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f"User {coworker.email} not found in user table")
                )
