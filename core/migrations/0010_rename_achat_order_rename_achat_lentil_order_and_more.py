# Generated by Django 4.2 on 2023-04-05 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_rename_totale_achat_total_alter_lentil_eye_choice_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Achat",
            new_name="Order",
        ),
        migrations.RenameField(
            model_name="lentil",
            old_name="achat",
            new_name="order",
        ),
        migrations.RenameField(
            model_name="menture",
            old_name="achat",
            new_name="order",
        ),
        migrations.RenameField(
            model_name="photoclient",
            old_name="achat",
            new_name="order",
        ),
        migrations.RenameField(
            model_name="progressif",
            old_name="achat",
            new_name="order",
        ),
    ]
