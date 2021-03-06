# Generated by Django 4.0.4 on 2022-05-05 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0002_personnel_alter_machine_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='Nom',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'MAc - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines'), ('Switch', 'Switch - To maintains and connect servers')], default='PC', max_length=32),
        ),
        migrations.AddField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 7, 46, 9, 36570)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='num_secu',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
