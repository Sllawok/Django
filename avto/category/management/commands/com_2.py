from django.core.management.base import BaseCommand
from category.models import Category,Tag, Post
class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Команда2')
        # category = Category.objects.get(name='Avto')
        Category.objects.create(name = 'NEW',description = 'что-то')
        print('Команда2')