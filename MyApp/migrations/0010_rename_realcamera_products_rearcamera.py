# Generated by Django 4.1 on 2022-11-03 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_products_battery_products_externalstorage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='RealCamera',
            new_name='RearCamera',
        ),
    ]