# Generated by Django 5.1.3 on 2024-11-25 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("im", "0003_alter_sale_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventory",
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
                ("date", models.DateField(help_text="Date of the inventory record")),
                (
                    "inventory_level",
                    models.PositiveIntegerField(
                        help_text="Current stock level of the product in the store"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="inventories",
                        to="im.product",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="inventories",
                        to="im.store",
                    ),
                ),
            ],
        ),
    ]
