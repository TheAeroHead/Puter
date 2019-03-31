from django.core.management.base import BaseCommand, CommandError
from products.models import Item

class Command(BaseCommand):
    help = "Adds test items to database"

    def handle(self, *args, **options):
        test = Item(name='testName2', description='testDescrip', price="3.50", category='test', image="images/jeffy.jpg")
        test.save()
