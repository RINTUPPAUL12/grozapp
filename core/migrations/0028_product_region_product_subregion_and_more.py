# Generated by Django 4.2 on 2023-04-13 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_remove_product_region_remove_product_subregion'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
        migrations.AddField(
            model_name='product',
            name='subregion',
            field=models.ManyToManyField(to='core.subregion'),
        ),
        migrations.AlterField(
            model_name='productregion',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='egion', to='core.product'),
        ),
    ]
