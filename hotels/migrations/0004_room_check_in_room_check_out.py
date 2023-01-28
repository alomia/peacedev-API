# Generated by Django 4.0.8 on 2023-01-28 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_rate_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='check_in',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='room',
            name='check_out',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]