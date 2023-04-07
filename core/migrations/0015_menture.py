# Generated by Django 4.2 on 2023-04-05 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_glass_alter_progressif_order_delete_menture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menture",
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
                (
                    "matiere",
                    models.CharField(
                        choices=[
                            ("PLASTIQUE", "PLASTIQUE"),
                            ("METALIQUE", "METALIQUE"),
                            ("SOLAIRE", "SOLAIRE"),
                        ],
                        max_length=15,
                        verbose_name="Matiére",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.order",
                        verbose_name="Client",
                    ),
                ),
            ],
        ),
    ]