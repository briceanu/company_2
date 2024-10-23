# Generated by Django 4.2.14 on 2024-10-21 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shift', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='driver_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shift',
            name='truck_used',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='truck.truck'),
        ),
    ]