# Generated by Django 4.1 on 2022-09-14 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_alter_user_managers_remove_user_username_and_more"),
        ("neuro", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sj",
            name="athlete",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="SJ",
                to="users.athlete",
            ),
        ),
    ]
