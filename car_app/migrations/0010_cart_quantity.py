# Generated by Django 4.2.5 on 2023-09-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0009_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
