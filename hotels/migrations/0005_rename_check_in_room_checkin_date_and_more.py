# Generated by Django 4.0.8 on 2023-01-28 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0004_room_check_in_room_check_out"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="check_in",
            new_name="checkin_date",
        ),
        migrations.RenameField(
            model_name="room",
            old_name="check_out",
            new_name="checkout_date",
        ),
    ]
