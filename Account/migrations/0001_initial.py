# Generated by Django 3.2.9 on 2021-12-05 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_service', models.CharField(choices=[('1', ''), ('2', 'Verizon'), ('3', 'T-Mobile'), ('4', 'AT&T')], default='1', max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]