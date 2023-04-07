# Generated by Django 4.2 on 2023-04-05 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_remove_order_type_de_verre_menture_type_de_verre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Glass",
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
                    "eye_choice",
                    models.CharField(
                        choices=[("OD", "OD"), ("OG", "OG")],
                        max_length=2,
                        verbose_name="OEUIL",
                    ),
                ),
                (
                    "spher",
                    models.CharField(
                        choices=[
                            ("PLAN", "PLAN"),
                            ("+ 0.00", "+ 0.00"),
                            ("+ 0.25", "+ 0.25"),
                            ("+ 0.5", "+ 0.5"),
                            ("+ 0.75", "+ 0.75"),
                            ("+ 1.00", "+ 1.00"),
                            ("+ 1.25", "+ 1.25"),
                            ("+ 1.5", "+ 1.5"),
                            ("+ 1.75", "+ 1.75"),
                            ("+ 2.00", "+ 2.00"),
                            ("+ 2.25", "+ 2.25"),
                            ("+ 2.5", "+ 2.5"),
                            ("+ 2.75", "+ 2.75"),
                            ("+ 3.00", "+ 3.00"),
                            ("+ 3.25", "+ 3.25"),
                            ("+ 3.5", "+ 3.5"),
                            ("+ 3.75", "+ 3.75"),
                            ("+ 4.00", "+ 4.00"),
                            ("+ 4.25", "+ 4.25"),
                            ("+ 4.5", "+ 4.5"),
                            ("+ 4.75", "+ 4.75"),
                            ("+ 5.00", "+ 5.00"),
                            ("+ 5.25", "+ 5.25"),
                            ("+ 5.5", "+ 5.5"),
                            ("+ 5.75", "+ 5.75"),
                            ("+ 6.00", "+ 6.00"),
                            ("+ 6.25", "+ 6.25"),
                            ("+ 6.5", "+ 6.5"),
                            ("+ 6.75", "+ 6.75"),
                            ("+ 7.00", "+ 7.00"),
                            ("+ 7.25", "+ 7.25"),
                            ("+ 7.5", "+ 7.5"),
                            ("+ 8.00", "+ 8.00"),
                            ("+ 8.25", "+ 8.25"),
                            ("+ 8.5", "+ 8.5"),
                            ("+ 8.75", "+ 8.75"),
                            ("+ 9.00", "+ 9.00"),
                            ("+ 9.25", "+ 9.25"),
                            ("+ 9.5", "+ 9.5"),
                            ("+ 9.75", "+ 9.75"),
                            ("+ 10.00", "+ 10.00"),
                            ("+ 10.25", "+ 10.25"),
                            ("+ 10.5", "+ 10.5"),
                            ("+ 10.75", "+ 10.75"),
                            ("+ 11.00", "+ 11.00"),
                            ("+ 11.25", "+ 11.25"),
                            ("+ 11.5", "+ 11.5"),
                            ("+ 11.75", "+ 11.75"),
                            ("+ 12.00", "+ 12.00"),
                            ("+ 12.25", "+ 12.25"),
                            ("+ 12.5", "+ 12.5"),
                            ("+ 12.75", "+ 12.75"),
                            ("+ 13.00", "+ 13.00"),
                            ("+ 13.25", "+ 13.25"),
                            ("+ 13.5", "+ 13.5"),
                            ("+ 13.75", "+ 13.75"),
                            ("+ 14.00", "+ 14.00"),
                            ("+ 14.25", "+ 14.25"),
                            ("+ 14.5", "+ 14.5"),
                            ("+ 14.75", "+ 14.75"),
                            ("+ 15.00", "+ 15.00"),
                            ("+ 15.25", "+ 15.25"),
                            ("+ 15.5", "+ 15.5"),
                            ("+ 15.75", "+ 15.75"),
                            ("+ 16.00", "+ 16.00"),
                            ("+ 16.25", "+ 16.25"),
                            ("+ 16.5", "+ 16.5"),
                            ("+ 16.75", "+ 16.75"),
                            ("+ 17.00", "+ 17.00"),
                            ("+ 17.25", "+ 17.25"),
                            ("+ 17.5", "+ 17.5"),
                            ("+ 17.75", "+ 17.75"),
                            ("+ 18.00", "+ 18.00"),
                            ("+ 18.25", "+ 18.25"),
                            ("+ 18.5", "+ 18.5"),
                            ("+ 18.75", "+ 18.75"),
                            ("+ 19.00", "+ 19.00"),
                            ("+ 19.25", "+ 19.25"),
                            ("+ 19.5", "+ 19.5"),
                            ("+ 19.75", "+ 19.75"),
                            ("+ 20.00", "+ 20.00"),
                            ("+ 20.25", "+ 20.25"),
                            ("+ 20.5", "+ 20.5"),
                            ("+ 20.75", "+ 20.75"),
                            ("+ 21.00", "+ 21.00"),
                            ("+ 21.25", "+ 21.25"),
                            ("+ 21.5", "+ 21.5"),
                            ("+ 21.75", "+ 21.75"),
                            ("+ 22.00", "+ 22.00"),
                            ("+ 22.25", "+ 22.25"),
                            ("+ 22.5", "+ 22.5"),
                            ("+ 22.75", "+ 22.75"),
                            ("+ 23.00", "+ 23.00"),
                            ("+ 23.25", "+ 23.25"),
                            ("+ 23.5", "+ 23.5"),
                            ("+ 23.75", "+ 23.75"),
                            ("+ 24.00", "+ 24.00"),
                            ("+ 24.25", "+ 24.25"),
                            ("+ 24.5", "+ 24.5"),
                            ("+ 24.75", "+ 24.75"),
                            ("+ 25.00", "+ 25.00"),
                            ("+ 25.25", "+ 25.25"),
                            ("+ 25.5", "+ 25.5"),
                            ("+ 25.75", "+ 25.75"),
                            ("+ 26.00", "+ 26.00"),
                            ("+ 26.25", "+ 26.25"),
                            ("+ 26.5", "+ 26.5"),
                            ("+ 26.75", "+ 26.75"),
                            ("+ 27.00", "+ 27.00"),
                            ("+ 27.25", "+ 27.25"),
                            ("+ 27.5", "+ 27.5"),
                            ("+ 27.75", "+ 27.75"),
                            ("+ 28.00", "+ 28.00"),
                            ("+ 28.25", "+ 28.25"),
                            ("+ 28.5", "+ 28.5"),
                            ("+ 28.75", "+ 28.75"),
                            ("+ 29.00", "+ 29.00"),
                            ("+ 29.25", "+ 29.25"),
                            ("+ 29.5", "+ 29.5"),
                            ("+ 29.75", "+ 29.75"),
                            ("+ 30.00", "+ 30.00"),
                            ("+ 30.25", "+ 30.25"),
                            ("+ 30.5", "+ 30.5"),
                            ("+ 30.75", "+ 30.75"),
                            ("+ 31.00", "+ 31.00"),
                            ("+ 31.25", "+ 31.25"),
                            ("+ 31.5", "+ 31.5"),
                            ("+ 31.75", "+ 31.75"),
                            ("+ 32.00", "+ 32.00"),
                            ("+ 32.25", "+ 32.25"),
                            ("+ 32.5", "+ 32.5"),
                            ("+ 32.75", "+ 32.75"),
                            ("+ 33.00", "+ 33.00"),
                            ("+ 33.25", "+ 33.25"),
                            ("+ 33.5", "+ 33.5"),
                            ("+ 33.75", "+ 33.75"),
                            ("+ 34.00", "+ 34.00"),
                            ("+ 34.25", "+ 34.25"),
                            ("+ 34.5", "+ 34.5"),
                            ("+ 34.75", "+ 34.75"),
                            ("+ 35.00", "+ 35.00"),
                            ("+ 35.25", "+ 35.25"),
                            ("+ 35.5", "+ 35.5"),
                            ("+ 35.75", "+ 35.75"),
                            ("+ 36.00", "+ 36.00"),
                            ("+ 36.25", "+ 36.25"),
                            ("+ 36.5", "+ 36.5"),
                            ("+ 36.75", "+ 36.75"),
                            ("+ 37.00", "+ 37.00"),
                            ("+ 37.25", "+ 37.25"),
                            ("+ 37.5", "+ 37.5"),
                            ("+ 37.75", "+ 37.75"),
                            ("+ 38.00", "+ 38.00"),
                            ("+ 38.25", "+ 38.25"),
                            ("+ 38.5", "+ 38.5"),
                            ("+ 38.75", "+ 38.75"),
                            ("+ 39.00", "+ 39.00"),
                            ("+ 39.25", "+ 39.25"),
                            ("+ 39.5", "+ 39.5"),
                            ("+ 39.75", "+ 39.75"),
                            ("+ 40.00", "+ 40.00"),
                            ("+ 40.25", "+ 40.25"),
                            ("+ 40.5", "+ 40.5"),
                            ("+ 40.75", "+ 40.75"),
                            ("- 0.00", "- 0.00"),
                            ("- 0.25", "- 0.25"),
                            ("- 0.5", "- 0.5"),
                            ("- 0.75", "- 0.75"),
                            ("- 1.00", "- 1.00"),
                            ("- 1.25", "- 1.25"),
                            ("- 1.5", "- 1.5"),
                            ("- 1.75", "- 1.75"),
                            ("- 2.00", "- 2.00"),
                            ("- 2.25", "- 2.25"),
                            ("- 2.5", "- 2.5"),
                            ("- 2.75", "- 2.75"),
                            ("- 3.00", "- 3.00"),
                            ("- 3.25", "- 3.25"),
                            ("- 3.5", "- 3.5"),
                            ("- 3.75", "- 3.75"),
                            ("- 4.00", "- 4.00"),
                            ("- 4.25", "- 4.25"),
                            ("- 4.5", "- 4.5"),
                            ("- 4.75", "- 4.75"),
                            ("- 5.00", "- 5.00"),
                            ("- 5.25", "- 5.25"),
                            ("- 5.5", "- 5.5"),
                            ("- 5.75", "- 5.75"),
                            ("- 6.00", "- 6.00"),
                            ("- 6.25", "- 6.25"),
                            ("- 6.5", "- 6.5"),
                            ("- 6.75", "- 6.75"),
                            ("- 7.00", "- 7.00"),
                            ("- 7.25", "- 7.25"),
                            ("- 7.5", "- 7.5"),
                            ("- 8.00", "- 8.00"),
                            ("- 8.25", "- 8.25"),
                            ("- 8.5", "- 8.5"),
                            ("- 8.75", "- 8.75"),
                            ("- 9.00", "- 9.00"),
                            ("- 9.25", "- 9.25"),
                            ("- 9.5", "- 9.5"),
                            ("- 9.75", "- 9.75"),
                            ("- 10.00", "- 10.00"),
                            ("- 10.25", "- 10.25"),
                            ("- 10.5", "- 10.5"),
                            ("- 10.75", "- 10.75"),
                            ("- 11.00", "- 11.00"),
                            ("- 11.25", "- 11.25"),
                            ("- 11.5", "- 11.5"),
                            ("- 11.75", "- 11.75"),
                            ("- 12.00", "- 12.00"),
                            ("- 12.25", "- 12.25"),
                            ("- 12.5", "- 12.5"),
                            ("- 12.75", "- 12.75"),
                            ("- 13.00", "- 13.00"),
                            ("- 13.25", "- 13.25"),
                            ("- 13.5", "- 13.5"),
                            ("- 13.75", "- 13.75"),
                            ("- 14.00", "- 14.00"),
                            ("- 14.25", "- 14.25"),
                            ("- 14.5", "- 14.5"),
                            ("- 14.75", "- 14.75"),
                            ("- 15.00", "- 15.00"),
                            ("- 15.25", "- 15.25"),
                            ("- 15.5", "- 15.5"),
                            ("- 15.75", "- 15.75"),
                            ("- 16.00", "- 16.00"),
                            ("- 16.25", "- 16.25"),
                            ("- 16.5", "- 16.5"),
                            ("- 16.75", "- 16.75"),
                            ("- 17.00", "- 17.00"),
                            ("- 17.25", "- 17.25"),
                            ("- 17.5", "- 17.5"),
                            ("- 17.75", "- 17.75"),
                            ("- 18.00", "- 18.00"),
                            ("- 18.25", "- 18.25"),
                            ("- 18.5", "- 18.5"),
                            ("- 18.75", "- 18.75"),
                            ("- 19.00", "- 19.00"),
                            ("- 19.25", "- 19.25"),
                            ("- 19.5", "- 19.5"),
                            ("- 19.75", "- 19.75"),
                            ("- 20.00", "- 20.00"),
                            ("- 20.25", "- 20.25"),
                            ("- 20.5", "- 20.5"),
                            ("- 20.75", "- 20.75"),
                            ("- 21.00", "- 21.00"),
                            ("- 21.25", "- 21.25"),
                            ("- 21.5", "- 21.5"),
                            ("- 21.75", "- 21.75"),
                            ("- 22.00", "- 22.00"),
                            ("- 22.25", "- 22.25"),
                            ("- 22.5", "- 22.5"),
                            ("- 22.75", "- 22.75"),
                            ("- 23.00", "- 23.00"),
                            ("- 23.25", "- 23.25"),
                            ("- 23.5", "- 23.5"),
                            ("- 23.75", "- 23.75"),
                            ("- 24.00", "- 24.00"),
                            ("- 24.25", "- 24.25"),
                            ("- 24.5", "- 24.5"),
                            ("- 24.75", "- 24.75"),
                            ("- 25.00", "- 25.00"),
                            ("- 25.25", "- 25.25"),
                            ("- 25.5", "- 25.5"),
                            ("- 25.75", "- 25.75"),
                            ("- 26.00", "- 26.00"),
                            ("- 26.25", "- 26.25"),
                            ("- 26.5", "- 26.5"),
                            ("- 26.75", "- 26.75"),
                            ("- 27.00", "- 27.00"),
                            ("- 27.25", "- 27.25"),
                            ("- 27.5", "- 27.5"),
                            ("- 27.75", "- 27.75"),
                            ("- 28.00", "- 28.00"),
                            ("- 28.25", "- 28.25"),
                            ("- 28.5", "- 28.5"),
                            ("- 28.75", "- 28.75"),
                            ("- 29.00", "- 29.00"),
                            ("- 29.25", "- 29.25"),
                            ("- 29.5", "- 29.5"),
                            ("- 29.75", "- 29.75"),
                            ("- 30.00", "- 30.00"),
                            ("- 30.25", "- 30.25"),
                            ("- 30.5", "- 30.5"),
                            ("- 30.75", "- 30.75"),
                            ("- 31.00", "- 31.00"),
                            ("- 31.25", "- 31.25"),
                            ("- 31.5", "- 31.5"),
                            ("- 31.75", "- 31.75"),
                            ("- 32.00", "- 32.00"),
                            ("- 32.25", "- 32.25"),
                            ("- 32.5", "- 32.5"),
                            ("- 32.75", "- 32.75"),
                            ("- 33.00", "- 33.00"),
                            ("- 33.25", "- 33.25"),
                            ("- 33.5", "- 33.5"),
                            ("- 33.75", "- 33.75"),
                            ("- 34.00", "- 34.00"),
                            ("- 34.25", "- 34.25"),
                            ("- 34.5", "- 34.5"),
                            ("- 34.75", "- 34.75"),
                            ("- 35.00", "- 35.00"),
                            ("- 35.25", "- 35.25"),
                            ("- 35.5", "- 35.5"),
                            ("- 35.75", "- 35.75"),
                            ("- 36.00", "- 36.00"),
                            ("- 36.25", "- 36.25"),
                            ("- 36.5", "- 36.5"),
                            ("- 36.75", "- 36.75"),
                            ("- 37.00", "- 37.00"),
                            ("- 37.25", "- 37.25"),
                            ("- 37.5", "- 37.5"),
                            ("- 37.75", "- 37.75"),
                            ("- 38.00", "- 38.00"),
                            ("- 38.25", "- 38.25"),
                            ("- 38.5", "- 38.5"),
                            ("- 38.75", "- 38.75"),
                            ("- 39.00", "- 39.00"),
                            ("- 39.25", "- 39.25"),
                            ("- 39.5", "- 39.5"),
                            ("- 39.75", "- 39.75"),
                            ("- 40.00", "- 40.00"),
                            ("- 40.25", "- 40.25"),
                            ("- 40.5", "- 40.5"),
                            ("- 40.75", "- 40.75"),
                        ],
                        default="PLAN",
                        max_length=10,
                    ),
                ),
                (
                    "cyl",
                    models.CharField(
                        choices=[
                            ("+ 0.00", "+ 0.00"),
                            ("+ 0.25", "+ 0.25"),
                            ("+ 0.5", "+ 0.5"),
                            ("+ 0.75", "+ 0.75"),
                            ("+ 1.00", "+ 1.00"),
                            ("+ 1.25", "+ 1.25"),
                            ("+ 1.5", "+ 1.5"),
                            ("+ 1.75", "+ 1.75"),
                            ("+ 2.00", "+ 2.00"),
                            ("+ 2.25", "+ 2.25"),
                            ("+ 2.5", "+ 2.5"),
                            ("+ 2.75", "+ 2.75"),
                            ("+ 3.00", "+ 3.00"),
                            ("+ 3.25", "+ 3.25"),
                            ("+ 3.5", "+ 3.5"),
                            ("+ 3.75", "+ 3.75"),
                            ("+ 4.00", "+ 4.00"),
                            ("+ 4.25", "+ 4.25"),
                            ("+ 4.5", "+ 4.5"),
                            ("+ 4.75", "+ 4.75"),
                            ("+ 5.00", "+ 5.00"),
                            ("+ 5.25", "+ 5.25"),
                            ("+ 5.5", "+ 5.5"),
                            ("+ 5.75", "+ 5.75"),
                            ("+ 6.00", "+ 6.00"),
                            ("+ 6.25", "+ 6.25"),
                            ("+ 6.5", "+ 6.5"),
                            ("+ 6.75", "+ 6.75"),
                            ("+ 7.00", "+ 7.00"),
                            ("+ 7.25", "+ 7.25"),
                            ("+ 7.5", "+ 7.5"),
                            ("+ 8.00", "+ 8.00"),
                            ("+ 8.25", "+ 8.25"),
                            ("+ 8.5", "+ 8.5"),
                            ("+ 8.75", "+ 8.75"),
                            ("+ 9.00", "+ 9.00"),
                            ("+ 9.25", "+ 9.25"),
                            ("+ 9.5", "+ 9.5"),
                            ("+ 9.75", "+ 9.75"),
                            ("+ 10.00", "+ 10.00"),
                            ("- 0.00", "- 0.00"),
                            ("- 0.25", "- 0.25"),
                            ("- 0.5", "- 0.5"),
                            ("- 0.75", "- 0.75"),
                            ("- 1.00", "- 1.00"),
                            ("- 1.25", "- 1.25"),
                            ("- 1.5", "- 1.5"),
                            ("- 1.75", "- 1.75"),
                            ("- 2.00", "- 2.00"),
                            ("- 2.25", "- 2.25"),
                            ("- 2.5", "- 2.5"),
                            ("- 2.75", "- 2.75"),
                            ("- 3.00", "- 3.00"),
                            ("- 3.25", "- 3.25"),
                            ("- 3.5", "- 3.5"),
                            ("- 3.75", "- 3.75"),
                            ("- 4.00", "- 4.00"),
                            ("- 4.25", "- 4.25"),
                            ("- 4.5", "- 4.5"),
                            ("- 4.75", "- 4.75"),
                            ("- 5.00", "- 5.00"),
                            ("- 5.25", "- 5.25"),
                            ("- 5.5", "- 5.5"),
                            ("- 5.75", "- 5.75"),
                            ("- 6.00", "- 6.00"),
                            ("- 6.25", "- 6.25"),
                            ("- 6.5", "- 6.5"),
                            ("- 6.75", "- 6.75"),
                            ("- 7.00", "- 7.00"),
                            ("- 7.25", "- 7.25"),
                            ("- 7.5", "- 7.5"),
                            ("- 8.00", "- 8.00"),
                            ("- 8.25", "- 8.25"),
                            ("- 8.5", "- 8.5"),
                            ("- 8.75", "- 8.75"),
                            ("- 9.00", "- 9.00"),
                            ("- 9.25", "- 9.25"),
                            ("- 9.5", "- 9.5"),
                            ("- 9.75", "- 9.75"),
                            ("- 10.00", "- 10.00"),
                        ],
                        default="+ 0.00",
                        max_length=10,
                    ),
                ),
                ("axe", models.IntegerField(default=0)),
                ("note", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date de Création"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date de dernière mise à jour"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.order",
                        verbose_name="glasses",
                    ),
                ),
                (
                    "type_de_verre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.glasstype",
                        verbose_name=" Type de verre",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="progressif",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.order",
                verbose_name="glasses",
            ),
        ),
        migrations.DeleteModel(
            name="Menture",
        ),
    ]
