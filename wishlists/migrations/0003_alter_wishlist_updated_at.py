# Generated by Django 4.0.8 on 2022-12-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_alter_wishlist_experiences_alter_wishlist_rooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
