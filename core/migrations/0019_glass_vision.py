# Generated by Django 4.2 on 2023-04-05 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_alter_order_ordonnance_return_alter_order_paid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="glass",
            name="vision",
            field=models.CharField(
                blank=True,
                choices=[("PRES", "PRES"), ("LOIN", "LOIN")],
                max_length=10,
                null=True,
                verbose_name="vision",
            ),
        ),
    ]
