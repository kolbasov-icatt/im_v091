# Generated by Django 5.1.3 on 2024-12-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("im", "0019_product_subcategory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="region",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
