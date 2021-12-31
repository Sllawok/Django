from django.core.management.base import BaseCommand
from category.models import Category,Tag, Post
class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.all()
        for i in categories:
            print('Команда_1',i)