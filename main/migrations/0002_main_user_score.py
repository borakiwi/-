# Generated by Django 4.2 on 2023-05-01 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="main_user",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]