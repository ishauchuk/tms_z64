# Generated by Django 4.0.2 on 2022-03-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_alter_product_options_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('BYN', 'Rubles'), ('USD', 'Dollars'), ('EUR', 'Euro')], default='BYN', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, max_length=3),
        ),
    ]
