# Generated by Django 4.2 on 2023-04-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_rename_subregion_product_subregion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Region',
        ),
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.ManyToManyField(to='core.region'),
        ),
    ]
