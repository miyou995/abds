# Generated by Django 4.2 on 2023-09-20 10:43

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0004_magasin_principale"),
        ("core", "0046_bouirasalesummary_alter_order_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="magasin",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="business.magasin",
                verbose_name="Magasin",
            ),
        ),
        migrations.AlterField(
            model_name="glassdeloin",
            name="cyl",
            field=models.CharField(
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
                    ("+ 7.75", "+ 7.75"),
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
                    ("- 7.75", "- 7.75"),
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
        migrations.AlterField(
            model_name="glassdeloin",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="de_loin_glasses",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="glassdeloin",
            name="type_de_verre",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="deloin_types_glass",
                to="core.glasstype",
                verbose_name=" Type de verre",
            ),
        ),
        migrations.AlterField(
            model_name="glassdepres",
            name="cyl",
            field=models.CharField(
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
                    ("+ 7.75", "+ 7.75"),
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
                    ("- 7.75", "- 7.75"),
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
        migrations.AlterField(
            model_name="glassdepres",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="de_pres_glasses",
                to="core.order",
                verbose_name="de_pres_glasses",
            ),
        ),
        migrations.AlterField(
            model_name="glassdepres",
            name="type_de_verre",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="depres_types_glass",
                to="core.glasstype",
                verbose_name=" Type de verre",
            ),
        ),
        migrations.AlterField(
            model_name="lentil",
            name="cyl",
            field=models.CharField(
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
                    ("+ 7.75", "+ 7.75"),
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
                    ("- 7.75", "- 7.75"),
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
        migrations.AlterField(
            model_name="lentil",
            name="lentil_type",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.lentiltype",
                verbose_name="Type de lentille",
            ),
        ),
        migrations.AlterField(
            model_name="lentil",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lentilles",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="menture",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.order",
                verbose_name="Client",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="client",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="core.client",
            ),
        ),
        migrations.AlterField(
            model_name="photoclient",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="progressifdeloin",
            name="cyl",
            field=models.CharField(
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
                    ("+ 7.75", "+ 7.75"),
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
                    ("- 7.75", "- 7.75"),
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
        migrations.AlterField(
            model_name="progressifdeloin",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="de_loin_progressifs",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="progressifdeloin",
            name="type_de_verre",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="progressif_deloin_types_glass",
                to="core.glasstype",
                verbose_name=" Type de verre",
            ),
        ),
        migrations.AlterField(
            model_name="progressifdepres",
            name="cyl",
            field=models.CharField(
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
                    ("+ 7.75", "+ 7.75"),
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
                    ("- 7.75", "- 7.75"),
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
        migrations.AlterField(
            model_name="progressifdepres",
            name="order",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="de_pres_progressifs",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="progressifdepres",
            name="type_de_verre",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="progressif_depres_types_glass",
                to="core.glasstype",
                verbose_name=" Type de verre",
            ),
        ),
    ]
