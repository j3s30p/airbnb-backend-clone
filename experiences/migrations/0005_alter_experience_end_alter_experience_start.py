# Generated by Django 4.1.2 on 2022-11-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0004_rename_perks_perk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="end",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="experience",
            name="start",
            field=models.DateTimeField(),
        ),
    ]