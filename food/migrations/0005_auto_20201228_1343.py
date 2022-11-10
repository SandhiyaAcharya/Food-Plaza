# Generated by Django 2.0.7 on 2020-12-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20201225_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='foodId',
            new_name='fid',
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='foodQuantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
    ]