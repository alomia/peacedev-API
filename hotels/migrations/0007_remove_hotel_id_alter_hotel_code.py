# Generated by Django 4.0.8 on 2023-01-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0006_remove_inventory_allotment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hotel",
            name="id",
        ),
        migrations.AlterField(
            model_name="hotel",
            name="code",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
