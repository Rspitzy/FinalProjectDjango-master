# Generated by Django 3.2.9 on 2021-12-05 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_service',
        ),
    ]