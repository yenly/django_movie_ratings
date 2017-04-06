from ratings.models import User
from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # future note: auto create anon users to match with ratings id up to 259137
        for x in range(1, 1400):
            new_user = User(id=x,email='anon@anon.com')
            new_user.save()
