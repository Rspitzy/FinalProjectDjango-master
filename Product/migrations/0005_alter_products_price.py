# Generated by Django 3.2.9 on 2021-12-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_rename_product_img_url_products_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
