# Generated by Django 4.1 on 2022-10-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_user_document"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="users/pictures"),
        ),
        migrations.AlterField(
            model_name="user",
            name="document",
            field=models.IntegerField(
                blank=True, null=True, unique=True, verbose_name="Cédula"
            ),
        ),
    ]
