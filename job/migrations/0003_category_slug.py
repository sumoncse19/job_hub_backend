# Generated by Django 4.2.5 on 2023-09-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]