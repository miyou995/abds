# Generated by Django 4.2 on 2023-04-06 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_glassdeloin_addition_glassdepres_addition_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="glassdepres",
            name="addition",
        ),
    ]
