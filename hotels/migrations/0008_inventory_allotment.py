# Generated by Django 4.0.8 on 2023-01-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0007_remove_hotel_id_alter_hotel_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventory",
            name="allotment",
            field=models.IntegerField(default=0),
        ),
    ]
