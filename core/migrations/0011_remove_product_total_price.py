# Generated by Django 4.1.7 on 2023-03-08 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_product_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
    ]