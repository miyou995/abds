# Generated by Django 4.2 on 2023-04-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_order_emergency"),
    ]

    operations = [
        migrations.AddField(
            model_name="lentil",
            name="diametre",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="lentil",
            name="rayon",
            field=models.IntegerField(default=0),
        ),
    ]
