# Generated by Django 4.1.2 on 2022-11-16 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0003_alter_booking_experiences_alter_booking_rooms_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="experiences",
            new_name="experience",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="rooms",
            new_name="room",
        ),
    ]
