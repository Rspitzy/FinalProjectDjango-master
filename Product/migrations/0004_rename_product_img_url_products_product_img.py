# Generated by Django 3.2.9 on 2021-12-06 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20211205_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_img_url',
            new_name='product_img',
        ),
    ]
