# Generated by Django 4.2.5 on 2023-09-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_upload_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_product',
            name='owner',
            field=models.CharField(choices=[('1st OWNER', 'owner1'), ('2nd OWNER', 'owner2'), ('3rd OWNER', 'owner3')], max_length=30),
        ),
    ]
