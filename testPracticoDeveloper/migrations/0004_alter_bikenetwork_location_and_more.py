# Generated by Django 4.2.2 on 2023-06-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testPracticoDeveloper', '0003_remove_extra_station_remove_location_bike_network_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikenetwork',
            name='location',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='bikenetwork',
            name='stations',
            field=models.JSONField(),
        ),
    ]
