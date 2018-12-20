# Generated by Django 2.1.4 on 2018-12-19 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_id', models.IntegerField()),
                ('compost_type', models.CharField(max_length=30)),
                ('compost_total', models.IntegerField()),
                ('compost_unit', models.CharField(max_length=30)),
                ('compost_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_record_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(max_length=200)),
                ('sensor', models.CharField(max_length=200)),
                ('start_plant_timestamp', models.DateTimeField()),
                ('end_plant_timestamp', models.DateTimeField()),
                ('create_record_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_harvested', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('create_record_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
    ]