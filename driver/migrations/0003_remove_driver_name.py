# Generated by Django 4.2.14 on 2024-10-17 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_alter_driver_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='name',
        ),
    ]
