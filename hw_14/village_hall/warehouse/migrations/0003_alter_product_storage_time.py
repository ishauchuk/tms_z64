# Generated by Django 4.0.2 on 2022-03-01 12:15

from django.db import migrations, models
import warehouse.models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_rename_wh_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='storage_time',
            field=models.DateField(validators=[warehouse.models.validate_storage_time]),
        ),
    ]
