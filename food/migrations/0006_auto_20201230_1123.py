# Generated by Django 2.0.7 on 2020-12-30 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20201228_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='foodQuantity',
            new_name='foodQty',
        ),
    ]
