# Generated by Django 4.1.2 on 2022-10-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Players",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=5)),
                ("minecraft_name", models.CharField(max_length=64)),
                ("discord_id", models.CharField(max_length=20)),
            ],
        ),
    ]
