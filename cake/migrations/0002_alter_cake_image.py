# Generated by Django 4.0 on 2021-12-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]