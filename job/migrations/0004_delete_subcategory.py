# Generated by Django 4.2.5 on 2023-09-14 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_category_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
