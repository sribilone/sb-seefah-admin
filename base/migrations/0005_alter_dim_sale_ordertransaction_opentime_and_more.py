# Generated by Django 4.1.5 on 2023-01-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_dim_sale_ordertransaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dim_sale_ordertransaction",
            name="opentime",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="dim_sale_ordertransaction",
            name="paidtime",
            field=models.TimeField(),
        ),
    ]
