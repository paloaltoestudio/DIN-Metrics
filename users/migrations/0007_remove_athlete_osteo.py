# Generated by Django 4.1 on 2022-08-26 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_athlete_osteo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='osteo',
        ),
    ]