# Generated by Django 5.1.2 on 2024-10-31 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productid',
        ),
    ]
