# Generated by Django 4.1 on 2022-09-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_orderhistorymodel_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderhistorymodel",
            name="total_price",
            field=models.FloatField(blank=True),
        ),
    ]
