# Generated by Django 4.2 on 2023-04-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0038_client_magasin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glassdeloin",
            name="addition",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Addition",
            ),
        ),
    ]
