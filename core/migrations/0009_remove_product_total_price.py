# Generated by Django 4.1.7 on 2023-03-08 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_attribute_attribute_attribute_product_region_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
    ]