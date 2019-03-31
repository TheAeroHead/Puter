from django.core.management.base import BaseCommand
from Puter.models import Item

class Command(BaseCommand):
    test = Item(name='testName', description='testDescrip', price="3.50", category='test')
    test.save

