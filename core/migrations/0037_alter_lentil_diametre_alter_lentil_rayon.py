# Generated by Django 4.2 on 2023-04-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0036_alter_lentil_brand_alter_lentil_diametre_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lentil",
            name="diametre",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="diametre"
            ),
        ),
        migrations.AlterField(
            model_name="lentil",
            name="rayon",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="rayon"
            ),
        ),
    ]