# Generated by Django 4.0.4 on 2022-06-12 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0003_rename_nom_personnel_nom_machine_mach_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 10, 27, 46, 679072)),
        ),
    ]