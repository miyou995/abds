# Generated by Django 4.2 on 2023-04-05 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_alter_glassdeloin_order_alter_glassdepres_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glassdeloin",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="de_loin_glasses",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="glassdepres",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="de_pres_glasses",
                to="core.order",
                verbose_name="de_pres_glasses",
            ),
        ),
        migrations.AlterField(
            model_name="lentil",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lentilles",
                to="core.order",
            ),
        ),
        migrations.AlterField(
            model_name="progressif",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="progressifs",
                to="core.order",
            ),
        ),
    ]