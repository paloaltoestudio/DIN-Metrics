# Generated by Django 4.1 on 2022-09-05 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0004_rename_test_fms_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fms',
            old_name='partial_score',
            new_name='score',
        ),
    ]
