# Generated by Django 4.2.5 on 2023-09-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='car_app/static')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('km', models.IntegerField()),
                ('price', models.IntegerField()),
                ('fuel', models.CharField(choices=[('PETROL', 'petrol'), ('DESEL', 'desel'), ('EV', 'ev')], max_length=30)),
                ('owner', models.CharField(choices=[('1st OWNER', '1st OWNER'), ('2nd OWNER', '2nd OWNER'), ('3rd OWNER', '3rd OWNER')], max_length=30)),
            ],
        ),
    ]
