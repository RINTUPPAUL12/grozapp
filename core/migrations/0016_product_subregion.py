# Generated by Django 4.1.7 on 2023-03-10 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_product_subregion_alter_subregion_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SubRegion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.subregion'),
            preserve_default=False,
        ),
    ]
