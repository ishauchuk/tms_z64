# Generated by Django 4.0.2 on 2022-03-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wh',
            new_name='Product',
        ),
    ]