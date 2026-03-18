from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.core.files import File
import os

class Command(BaseCommand):
    help = 'Seed database with categories and products with images'

    def handle(self, *args, **kwargs):
        electronics, _ = Category.objects.get_or_create(name="Electronics")
        fashion, _ = Category.objects.get_or_create(name="Fashion")


        base_path = 'media/core/'

        with open(os.path.join(base_path, 'laptop.jpg'), 'rb') as f:
            product, created = Product.objects.get_or_create(
                name="Apple Laptop",
                defaults={
                    "slug": "apple-laptop",
                    "category": electronics,
                    "price": 100000,
                    "description": "Original Apple laptop"
                }
            )
            if created:
                product.image.save('laptop.jpg', File(f), save=True)

        with open(os.path.join(base_path, 'shoes.jpg'), 'rb') as f:
            product, created = Product.objects.get_or_create(
                name="Nike Shoes",
                defaults={
                    "slug": "nike-shoes",
                    "category": fashion,
                    "price": 5000,
                    "description": "Comfortable running shoes"
                }
            )
            if created:
                product.image.save('shoes.jpg', File(f), save=True)

        with open(os.path.join(base_path, 'jeans.jpg'), 'rb') as f:
            product, created = Product.objects.get_or_create(
                name="Jeans",
                defaults={
                    "slug": "jeans",
                    "category": fashion,
                    "price": 2000,
                    "description": "Stylish denim jeans"
                }
            )
            if created:
                product.image.save('jeans.jpg', File(f), save=True)

        self.stdout.write(self.style.SUCCESS("Products with images created!"))