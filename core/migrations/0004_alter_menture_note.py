# Generated by Django 4.2 on 2023-04-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_menture_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menture",
            name="note",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]