# Generated by Django 4.1 on 2024-03-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student",
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
                ("cName", models.CharField(max_length=20)),
                ("cSex", models.CharField(default="M", max_length=2)),
                ("cPhone", models.CharField(blank=True, default="", max_length=50)),
                ("cAddr", models.CharField(blank=True, default="", max_length=255)),
                ("cBirthday", models.DateField()),
                ("cEmail", models.EmailField(blank=True, default="", max_length=100)),
            ],
        ),
    ]
