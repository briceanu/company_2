# Generated by Django 4.2.14 on 2024-10-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_remove_driver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]