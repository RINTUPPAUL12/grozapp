# Generated by Django 4.2 on 2023-04-10 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_product_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='SubRegion',
            new_name='subregion',
        ),
    ]
