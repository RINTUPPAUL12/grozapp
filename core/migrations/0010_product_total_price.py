# Generated by Django 4.1.7 on 2023-03-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_product_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.FloatField(default=0.0),
        ),
    ]
