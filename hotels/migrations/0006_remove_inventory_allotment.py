# Generated by Django 4.0.8 on 2023-01-28 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0005_rename_check_in_room_checkin_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventory",
            name="allotment",
        ),
    ]
