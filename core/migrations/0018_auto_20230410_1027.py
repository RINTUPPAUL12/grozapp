# Generated by Django 3.2.3 on 2023-04-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_product_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='SubRegion',
        ),
        migrations.AddField(
            model_name='product',
            name='SubRegion',
            field=models.ManyToManyField(to='core.SubRegion'),
        ),
    ]
