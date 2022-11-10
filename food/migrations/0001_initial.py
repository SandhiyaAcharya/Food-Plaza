# Generated by Django 2.0.7 on 2020-12-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('foodId', models.AutoField(primary_key=True, serialize=False)),
                ('foodName', models.CharField(max_length=30)),
                ('foodCat', models.CharField(max_length=50)),
                ('foodType', models.CharField(default='Indian', max_length=15)),
                ('foodPrice', models.FloatField(max_length=15)),
                ('foodQuantity', models.IntegerField(default=0)),
                ('foodImage', models.ImageField(default='', upload_to='media')),
            ],
            options={
                'db_table': 'Food',
            },
        ),
    ]