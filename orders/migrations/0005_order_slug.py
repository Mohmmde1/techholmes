# Generated by Django 4.2.10 on 2024-02-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_cart_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
