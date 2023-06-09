# Generated by Django 4.2 on 2023-04-07 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0004_magasin_principale"),
        ("core", "0037_alter_lentil_diametre_alter_lentil_rayon"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="magasin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="business.magasin",
                verbose_name="Magasin",
            ),
        ),
    ]
