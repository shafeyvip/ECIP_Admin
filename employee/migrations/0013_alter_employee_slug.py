# Generated by Django 5.0 on 2024-06-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_alter_employee_employee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
