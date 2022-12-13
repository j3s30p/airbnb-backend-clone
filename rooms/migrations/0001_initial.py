# Generated by Django 4.0.8 on 2022-12-13 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_alter_category_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('country', models.CharField(default='한국', max_length=50)),
                ('city', models.CharField(default='서울', max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('toilets', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=250)),
                ('pet_friendly', models.BooleanField(default=True)),
                ('kind', models.CharField(choices=[('entire_place', 'Entire place'), ('private_room', 'Private room'), ('shared_room', 'Shared room')], max_length=20)),
                ('amenities', models.ManyToManyField(related_name='rooms', to='rooms.amenity')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='categories.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
