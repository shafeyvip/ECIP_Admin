# Generated by Django 5.0 on 2024-06-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_employee_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.IntegerField(auto_created=True, default=1000, unique=True),
        ),
    ]
