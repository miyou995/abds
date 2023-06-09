# Generated by Django 4.2 on 2023-04-05 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_glassdeloin_glassdepres_delete_glass"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glassdeloin",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.order",
                verbose_name="de_loin_glasses",
            ),
        ),
        migrations.AlterField(
            model_name="glassdepres",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.order",
                verbose_name="de_pres_glasses",
            ),
        ),
    ]
