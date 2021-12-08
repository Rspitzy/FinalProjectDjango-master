# Generated by Django 3.2.9 on 2021-12-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20211205_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='alert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='product_img_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]