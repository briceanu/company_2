# Generated by Django 4.2.14 on 2024-10-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
