# Generated by Django 4.2 on 2023-04-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_lentil_diametre_lentil_rayon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lentil",
            name="axe",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Axe"
            ),
        ),
        migrations.AlterField(
            model_name="progressif",
            name="progressif",
            field=models.CharField(
                blank=True,
                choices=[("LOIN", "LOIN"), ("PRES", "PRES")],
                max_length=10,
                null=True,
            ),
        ),
    ]
