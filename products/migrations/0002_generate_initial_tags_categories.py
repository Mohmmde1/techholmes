# Generated by Django 4.2.10 on 2024-02-20 04:06

from django.db import migrations, transaction
from faker import Faker
from products.models import Category, Tag

import string

fake = Faker()


def generate_slug(name):
    # Remove spaces and convert to lowercase
    slug = name.lower().replace(' ', '-')
    # Remove special characters
    slug = ''.join(char for char in slug if char in string.ascii_lowercase or char in string.digits or char == '-')
    return slug

def generate_categories_and_tags(apps, schema_editor):
    num_categories = 10  
    num_tags = 20  
    with transaction.atomic():
        for _ in range(num_categories):
            name = fake.word()
            slug = generate_slug(name)
            Category.objects.create(name=name, slug=slug)

        for _ in range(num_tags):
            name = fake.word()
            slug = generate_slug(name)
            Tag.objects.create(name=name, slug=slug)
        
def reverse_categories_and_tags(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Tag = apps.get_model('products', 'Tag')

    # Delete all categories and tags
    Category.objects.all().delete()
    Tag.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_categories_and_tags, reverse_code=reverse_categories_and_tags)
    ]
