# Generated by Django 4.2.3 on 2023-07-18 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='sensor_id',
        ),
    ]
