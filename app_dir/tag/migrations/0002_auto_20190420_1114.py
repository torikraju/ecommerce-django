# Generated by Django 2.1.2 on 2019-04-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
