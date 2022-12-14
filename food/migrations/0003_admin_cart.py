# Generated by Django 2.0.7 on 2020-12-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminName', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adminPass', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cartId', models.AutoField(primary_key=True, serialize=False)),
                ('custEmail', models.CharField(max_length=30)),
                ('foodId', models.IntegerField()),
                ('foodQuantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cartSAP',
            },
        ),
    ]
