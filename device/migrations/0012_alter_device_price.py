# Generated by Django 5.0 on 2024-06-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0011_alter_device_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]