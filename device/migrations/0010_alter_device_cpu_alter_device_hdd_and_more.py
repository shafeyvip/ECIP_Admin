# Generated by Django 5.0 on 2024-06-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_alter_device_device_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='cpu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='hdd',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='motherboard',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='ram',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
