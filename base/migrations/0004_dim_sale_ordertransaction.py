# Generated by Django 4.1.5 on 2023-01-15 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_room_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="dim_sale_ordertransaction",
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
                ("transcomp_id", models.IntegerField()),
                ("shop_id", models.IntegerField()),
                ("opentime", models.DateTimeField()),
                ("paidtime", models.DateTimeField()),
                ("salemode", models.PositiveSmallIntegerField()),
                ("nocustomer", models.PositiveSmallIntegerField()),
                ("table_id", models.IntegerField()),
                ("totalretailprice", models.FloatField()),
                ("totalretailpriceb4vat", models.FloatField()),
                ("totalretailpricevat", models.FloatField()),
                ("discountprice", models.FloatField()),
                ("discountb4vat", models.FloatField()),
                ("totalamout", models.FloatField()),
                ("shopname", models.CharField(max_length=200)),
                ("membercode", models.CharField(max_length=200)),
                ("posshop_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
                ("calender_id", models.IntegerField()),
            ],
        ),
    ]
