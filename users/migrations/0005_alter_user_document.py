# Generated by Django 4.1 on 2022-08-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_athlete_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.IntegerField(null=True, unique=True, verbose_name='Cédula'),
        ),
    ]