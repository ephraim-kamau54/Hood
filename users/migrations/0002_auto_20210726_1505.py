# Generated by Django 3.2.5 on 2021-07-26 12:05

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.CharField(choices=[('1', 'Red Ville'), ('2', 'Green View'), ('3', 'The Park'), ('4', 'BEACH'), ('5', 'BMW'), ('6', 'Deer')], default='Red Ville', max_length=25),
        ),
    ]
