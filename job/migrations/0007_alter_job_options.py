# Generated by Django 4.2.5 on 2023-09-15 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('-created_at',)},
        ),
    ]
