from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавить продукт в БД'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'category.json')
        call_command('loaddata', 'product.json')
        category, _ = Category.objects.get_or_create(name='Комиксы', description='Рисованные истории')

        products = [
            {'name': 'Противостояние', 'description': 'По роману Стивена Кинга', 'category': category, 'purchase_price': '900', 'created_at': '2025-01-03', 'updated_at': '2025-01-03'},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Успешно добавлено: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product.name}'))