# Generated by Django 4.2.5 on 2023-09-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
