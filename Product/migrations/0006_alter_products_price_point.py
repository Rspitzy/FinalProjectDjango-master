# Generated by Django 3.2.9 on 2021-12-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]